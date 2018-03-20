"""TODO."""
import os

import pandas as pd
from dotenv import load_dotenv

from facebook_client import FacebookClient

load_dotenv()
fb = FacebookClient(access_token=os.getenv('FACEBOOK_ACCESS_TOKEN'))
nonprofit_df = pd.read_csv('nonprofit_facebook.csv')

nonprofit_df['fan_count'] = nonprofit_df['facebook'].map(fb.get_page_fan_count)
nonprofit_df['about'] = nonprofit_df['facebook'].map(fb.get_page_about)
nonprofit_df.to_csv('output.csv', index=False)
