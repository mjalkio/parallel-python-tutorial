"""TODO."""
import os

import facebook
from dotenv import load_dotenv

load_dotenv()

graph = facebook.GraphAPI(access_token=os.getenv('FACEBOOK_ACCESS_TOKEN'),
                          version='2.6')

print(graph.get_object(id='TheTaskForceforGlobalHealth',
                       fields='about,fan_count'))
