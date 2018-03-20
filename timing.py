"""TODO."""
import os
import time

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
