import tweepy
import datetime

consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret
)

api = tweepy.API(auth)

search_query = "load shedding stage"

tweets = []

for tweet in tweepy.Cursor(api.search_tweets, q=search_query).items():
    tweets.append(tweet)

# Sort the tweets by date
tweets.sort(key=lambda x: datetime.datetime.strptime(x.created_at, "%a %b %d %H:%M:%S %z %Y"))

for tweet in tweets:
    print(tweet.created_at, tweet.text)