__author__ = 'thomastosoni'

#API KEY FOR tosoni.thomas@gmail.com : 6440b901143b25027624c1a835e2cb91
#API SECRET FOR tosoni.thomas@gmail.com : lnsrNhJLj96Ds0ILLalqMjdwXR0eoPOqa9lyN1hLYOZ1gndQIz

from twython import Twython

APP_KEY = "6440b901143b25027624c1a835e2cb91"
APP_SECRET = "lnsrNhJLj96Ds0ILLalqMjdwXR0eoPOqa9lyN1hLYOZ1gndQIz"

twitter = Twython(APP_KEY, APP_SECRET)

auth = twitter.get_authentication_tokens()

print(twitter.search(q='twitter', result_type='popular'))

#http://api.twittercounter.com/?apikey=6440b901143b25027624c1a835e2cb91&twitter_id=15160529
