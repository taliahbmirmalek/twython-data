import json
from time import sleep
from django.utils import simplejson

__author__ = 'thomastosoni'

# API KEY FOR tosoni.thomas@gmail.com : 6440b901143b25027624c1a835e2cb91
#API SECRET FOR tosoni.thomas@gmail.com : lnsrNhJLj96Ds0ILLalqMjdwXR0eoPOqa9lyN1hLYOZ1gndQIz

from twython import Twython

APP_KEY = "XmM7DzeRDTifs438XZHAzWt00"
APP_SECRET = "PrN7O2tQ517HgJsiBKCDfAsP6YBXfgsOJx4BeK0AwOETdQNAlY"

## Twython
twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()
twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)

# Popular mtv tweets
# tweets = twitter.search(q='mtv', count='10', result_type='popular')
# for tweet in tweets['statuses']:
# 	print(tweet)
# 	sleep(0.2)

# Print Twitter's Terms of services
# tos = twitter.get_tos()
# print(tos)

#Print available trends locations
# output = twitter.get_available_trends()
# if output:
# 	for trend in output:
# 		print(trend)

#Print Toronto's Trends
# toronto = twitter.get_place_trends(id=4118)
# if toronto:
# 	for trend in toronto[0].get('trends'):
# 		print(trend)

#Print Worldwide Trends
# us = twitter.get_place_trends(id=1)
# if us:
# 	for trend in us[0].get('trends'):
# 		print(trend)

#Print closest location for trends to UCB (In this case: San Francisco)
# ucb = twitter.get_closest_trends(lat=37.8719530, long=-122.2600593)
# if ucb:
# 	for trends in ucb:
# 		print(trends)

