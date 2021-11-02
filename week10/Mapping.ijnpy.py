import tweepy
auth = tweepy.OAuthHandler('WaRIBOKDDjW33QOu17nVevyXN', '5fJRJEK4khl7MlACcxZltqK4Tnamo4pFqvq3PpwhbwfwhNInwP')
auth.set_access_token('1339345602438696961-Gvgo8eRfYg4mQ0GU2l3CTLecfk0zRE', 'wi4Tui4fY5JJ5wlydfBO8rL9V3N8s7uxz9G8bs6JgxULR')

api = tweepy.API(auth, wait_on_rate_limit=True)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

import pandas as pd

search_words = "#COVIDvaccine"
date_since = "2019-10-01"
tweets = tweepy.Cursor(api.search_tweets,
              q=search_words, lang="en").items(300)

tweets_sorted = [[tweet.user.screen_name, tweet.geo, tweet.user.location, tweet.text] for tweet in tweets]

tdf = pd.DataFrame(data=tweets_sorted, columns=['user', 'coordinates','location', 'tweet'])
print(tdf)


locs = tdf['location'].value_counts()
print(locs)

from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

geolocator = Nominatim(user_agent='twitter-analysis-client')
limited = RateLimiter(geolocator.geocode, min_delay_seconds=1)

def find_location(row):
    place = row['location']
    location = limited(place)
    
    if location != None:
        return location.latitude, location.longitude
    else:
        return "Not Found", "Not Found"

tdf[['latitude','longitude']] = tdf.apply(find_location, axis="columns", result_type="expand")
tdf
