# Import our Twitter credentials from credentials.py
from credentials import *
import time
import tweepy

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def tweet():
    with open('content.txt', 'r') as file_lines:
        for line in file_lines:
            try:
                print(line)
                if line != '\n':
                    api.update_status(line)
                    time.sleep(900)
                else:
                    pass
            except tweepy.TweepError as e:
                print(e.reason)
                time.sleep(2)


def query_twitter_for_tweets():
    # For loop to iterate over tweets with #ocean, limit to 10
    for tweet in tweepy.Cursor(api.search, q='#Python').items(10):
        # Print out usernames of the last 10 people to use #ocean
        try:
            print(tweet.text)
            print('Tweet by: @' + tweet.user.screen_name)
            print(tweet.user.following)
            # tweet.retweet() # retweet a given tweet
            # tweet.favorite() # favorite a given tweet
            #if not tweet.user.following:
                # tweet.user.follow() # follow the person who tweeted the given tweet
        except tweepy.TweepError as e:
            print(e.reason)

        except StopIteration:
            break


query_twitter_for_tweets()
