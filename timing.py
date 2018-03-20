"""TODO."""
import os
import time
from multiprocessing import Pool

import dask.dataframe as dd
import pandas as pd
from dotenv import load_dotenv

from facebook_client import FacebookClient

load_dotenv()
fb = FacebookClient(access_token=os.getenv('FACEBOOK_ACCESS_TOKEN'))
nonprofit_df = pd.read_csv('nonprofit_facebook.csv')

t0 = time.perf_counter()
nonprofit_df['facebook'].map(fb.get_page_fan_count)
nonprofit_df['facebook'].map(fb.get_page_about)
t1 = time.perf_counter()
print("Time elapsed: {time} seconds.".format(time=t1 - t0))

t0 = time.perf_counter()
with Pool(processes=4) as pool:
    pool.map(fb.get_page_fan_count, nonprofit_df['facebook'])
    pool.map(fb.get_page_about, nonprofit_df['facebook'])
t1 = time.perf_counter()
print("Time elapsed: {time} seconds.".format(time=t1 - t0))

nonprofit_df_dask = dd.read_csv('nonprofit_facebook.csv', blocksize=200)
t0 = time.perf_counter()
nonprofit_df_dask['facebook'].map(fb.get_page_fan_count,
                                  meta=('fan_count', int)).compute()
nonprofit_df_dask['facebook'].map(fb.get_page_about,
                                  meta=('about', str)).compute()
t1 = time.perf_counter()
print("Time elapsed: {time} seconds.".format(time=t1 - t0))
