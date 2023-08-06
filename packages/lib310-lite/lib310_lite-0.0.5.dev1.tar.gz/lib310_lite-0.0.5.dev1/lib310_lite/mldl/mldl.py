import numpy as np
import random
import time
import pandas as pd
from threading import Thread, Event
from queue import Queue
import concurrent.futures
from bounded_pool_executor import BoundedThreadPoolExecutor
import dask.dataframe as dd
from ..bigquery.client import Client as BigQueryClient
from ..bigquery.constants import FileFormat

# PGSQL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models.SeqLangModel import SeqLangModel
from .models.InteractionModel import InteractionModel


class MLDL:

    __TRAIN = 'TRAIN'
    __TEST = 'TEST'
    __VAL = 'VAL'
    __MAIN = 'MAIN'
    __INTERACTION = 'INTERACTION'
    __PARTS = {__INTERACTION: 1}

    def __init__(self, db_url: str, cache_size: int = 50, num_threads: int = 10, random_seed: int = time.time()):
        random.seed(random_seed)
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)

        self.bq_client = BigQueryClient()

        # self.collections = {
        #     MLDL.__TRAIN: {
        #         MLDL.__MAIN: self.db['seq_lang5_copy'],
        #         MLDL.__INTERACTION: self.db['interactions_lang5_train'],
        #     },
        #     MLDL.__TEST: {
        #         MLDL.__MAIN: self.db['seq_lang5_copy'],
        #         MLDL.__INTERACTION: self.db['interactions_lang5_test'],
        #     }
        # }

        # this is the pool of samples row_id
        self.sample_cache = []
        # this is the maximum number of requests we fetch sooner from the database
        self.max_queue_size = cache_size
        # this is the number of threads we use to fetch data from the database
        self.num_threads = num_threads
        # this is the key that we know MLDL requests are same or not if it changes we need to fetch new data
        self.queue_key = None
        # this is the key shows that pool is still valid or not
        self.pool_key = None
        # this is the queue that we use to cache requests and put it in the queue
        self.queue = Queue(self.max_queue_size)
        # this is the thread that we use to fill the queue
        self.filler_thread = None
        # this is the event that we use to kill the filler thread
        self.kill_event = Event()
        # this is the number of retries we have
        self.retry = 0

    def get_batch(self, num: int, max_length: int, min_num_feature: int = 0, stage: str = __TRAIN, parts: dict = None):
        """
        Get a batch of data from the database with regard to the length of the sequence and the number of features
        It also start the background thread to fill the caches and queue
        :param num: number of samples
        :param max_length: maximum length of the sequence
        :param min_num_feature: minimum number of features
        :param stage: TRAIN or TEST
        :param parts: the parts of the data that we want to fetch
        :return: a pandas dataframe
        """
        stage = stage.upper()
        # if stage == MLDL.__TRAIN:
        #     col = self.collections[MLDL.__TRAIN]
        # elif stage == MLDL.__TEST:
        #     col = self.collections[MLDL.__TEST]
        # else:
        #     raise ValueError('Stage must be either TRAIN or TEST')

        if parts is None:
            parts = MLDL.__PARTS

        hit = self.queue_key == f'{num}_{max_length}_{min_num_feature}_{stage}'
        if hit:
            # HIT
            return pd.DataFrame(self.queue.get())

        # MISS
        table = '1_uniprot.pg_lang5'
        
        if len(self.sample_cache) == 0 or not self.pool_key or self.pool_key != f'{max_length}_{min_num_feature}_{stage}':
            self.pool_key = f'{max_length}_{min_num_feature}_{stage}'
            res = self.bq_client.cache_query(
                query=f"SELECT row_id FROM `{table}` WHERE len <= {max_length} and token_size >= {min_num_feature} and stage = '{stage}'",
                name=f'{max_length}_{min_num_feature}_{stage}',
                destination_format=FileFormat.CSV
            )
            ddf = dd.read_csv(res['uri'])
            df = ddf.compute()
            self.sample_cache = df['row_id'].tolist()

        # killing the previous thread
        if self.filler_thread is not None:
            self.kill_event.set()
            self.queue.get()
            self.filler_thread.join()
            self.kill_event.clear()
            self.queue = Queue(self.max_queue_size)

        # generate new key
        self.queue_key = f'{num}_{max_length}_{min_num_feature}_{stage}'

        # start new thread
        self.filler_thread = Thread(target=self.filler, args=(num, stage, parts))
        self.filler_thread.start()
        time.sleep(3)
        return self.fetch_sample(num, stage, parts)

    def filler(self, num: int, stage: str, parts: dict = None):
        """
        This function is used to fill the queue with data then get batch read data from the queue
        :param num: number of samples
        :param stage: TRAIN or TEST
        :param parts: the parts of the data that we want to fetch
        """
        if parts is None:
            parts = MLDL.__PARTS
        with BoundedThreadPoolExecutor(max_workers=self.num_threads) as executor:
            while not self.kill_event.is_set():
                executor.submit(self.filler_worker, num, stage, parts)
            while not self.queue.empty():
                self.queue.get()
            executor.shutdown(wait=True)

    def filler_worker(self, num: int, stage: str, parts: dict = None):
        session = self.Session()
        if parts is None:
            parts = MLDL.__PARTS
        df = self.fetch_sample(num, stage, session, parts)
        self.queue.put(df)
        session.close()
        return

    def fetch_sample(self, num: int, stage: str, session, parts: dict = None):
        """
        This function is used to fetch the data from the database
        Run two threads to fetch the data from the database
        :param num: number of samples
        :param stage: TRAIN or TEST
        :param session: the session that we use to connect to the database
        :param parts: the parts of the data that we want to fetch
        :return: dataframe of the data
        """
        if parts is None:
            parts = MLDL.__PARTS
        try:
            # get random row_id from the pool
            index_list = random.sample(self.sample_cache, min(num, len(self.sample_cache)))

            with concurrent.futures.ThreadPoolExecutor() as executor:
                main_thread = executor.submit(self.fetch_sample_main, index_list, stage, session, parts)
                if parts[MLDL.__INTERACTION] and parts[MLDL.__INTERACTION] == 1:
                    interaction_thread = executor.submit(self.fetch_sample_interaction, index_list, session)

                main_df = main_thread.result()
                interaction_df = pd.DataFrame()
                if parts[MLDL.__INTERACTION] and parts[MLDL.__INTERACTION] == 1:
                    interaction_df = interaction_thread.result()

                if len(interaction_df) == 0:
                    main_df['interactions'] = np.nan
                    self.retry = 0
                    return main_df
                df = pd.merge(main_df, interaction_df, on='row_id', how='left')
                self.retry = 0
                return df
        except Exception as e:
            print(e)
            if self.retry == 0:
                time.sleep(1)
            else:
                time.sleep(self.retry * 10)
            self.retry += 1
            print(f'Cannot fetch data from database, retry number {self.retry} times')
            if self.retry > 7:
                raise Exception('Cannot fetch data from database')
            return self.fetch_sample(num, stage, session, parts)

    def fetch_sample_main(self, index_list: list, stage: str, session, parts: dict = None):
        """
        This function is used to fetch the main data from the database
        :param index_list: list of row_ids
        :param stage: stage of the data
        :param session: the session that we use to connect to the database
        :param parts: parts of the data
        :return: dataframe of main data
        """
        # session = self.Session()
        if parts is None:
            parts = MLDL.__PARTS
        try:
            results = session.query(SeqLangModel).filter(SeqLangModel.row_id.in_(index_list)).all()
            df = pd.DataFrame([r.to_dict() for r in results])
        except Exception as e:
            print(e)
            raise Exception('Cannot fetch data from database <SeqLang>')
        return df

    def fetch_sample_interaction(self, index_list: list, session):
        """
        This function is used to fetch the interaction data from the database
        :param index_list: list of row_ids
        :param session: the session that we use to connect to the database
        :return: dataframe of interaction data
        """
        # session = self.Session()
        try:
            results = session.query(InteractionModel).filter(InteractionModel.row_id.in_(index_list)).all()
            df = pd.DataFrame([r.to_dict() for r in results])
        except Exception as e:
            print(e)
            raise Exception('Cannot fetch data from database <Interaction>')
        return df

    def terminate(self):
        """
        Terminate the filler threads and clear the queue
        """
        # Terminate the filler thread
        if self.filler_thread is not None:
            self.kill_event.set()
            self.queue.get()
            self.filler_thread.join()
            self.kill_event.clear()
            self.queue = Queue(self.max_queue_size)
