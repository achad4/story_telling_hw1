import json
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

ACCESS_TOKEN = '4885882060-OPfhKlPKeGIwiGGQgyl5QzIj58v4tZ5JFKUOJli'
ACCESS_SECRET = 'VjXlFKHvDoj7mAcnkdWqMz8UcoTH1gtotIepDHna4uaPr'
CONSUMER_KEY = 'NkSHnhdfiHAhcG0jLeftJAB7m'
CONSUMER_SECRET = 'j0gyjgEsVbcQ2Lm5sETdEjnlsJTfcFOeJIkJZxSJpj7y64sxXG'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

twitter_stream = TwitterStream(auth=oauth)

iterator = twitter_stream.statuses.filter(track="kanye west", language="en")

tweet_count = 1000
for tweet in iterator:
    tweet_count -= 1
    print json.dumps(tweet)  
       
    if tweet_count <= 0:
        break