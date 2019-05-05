import re
import tweepy
from tweepy import OAuthHandler, Cursor
from textblob import TextBlob
from os import path as path
import yaml


class TwitterClient(object):
    ''' 
    Generic Twitter Class for sentiment analysis. 
    '''

    def __init__(self):
        ''' 
        Class constructor or initialization method. 
        '''
        # keys and tokens from the Twitter Dev Console

        # Fetching twitter keys
        self.get_twitter_keys()
        # attempt authentication
        try:
            # create OAuthHandler object
            self.auth = OAuthHandler(self.consumer_key, self.consumer_secret)
            # set access token and secret
            self.auth.set_access_token(
                self.access_token, self.access_token_secret)
            # create tweepy API object to fetch tweets
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")

    def get_twitter_keys(self):
        with open(path.join(path.abspath('.'), 'twitter-secret-keys.yaml'), 'r') as stream:
            try:
                entries = yaml.load_all(stream)
                for entry in entries:
                    for pair in entry.split():
                        key, value = pair.split(":")
                        if key == "API-Key":
                            self.consumer_key = value
                        elif key == "API-Secret-Key":
                            self.consumer_secret = value
                        elif key == "Access-Token":
                            self.access_token = value
                        elif key == "Access-Secret-Token":
                            self.access_token_secret = value
                        else:
                            print("Error in reading keys.. Debug and retry")
            except yaml.YAMLError as exc:
                print(exc)

    def clean_tweet(self, tweet):
        ''' 
        Utility function to clean tweet text by removing links, special characters 
        using simple regex statements. 
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z\t])|(\w+:\/\/\S+)", " ", tweet).split())

    def get_tweet_sentiment(self, tweet):
        ''' 
        Utility function to classify sentiment of passed tweet 
        using textblob's sentiment method 
        '''
        # create TextBlob object of passed tweet text
        analysis = TextBlob(self.clean_tweet(tweet))
        # set sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

    def get_tweets(self, query, count=10):
        ''' 
        Main function to fetch tweets and parse them. 
        '''
        # empty list to store parsed tweets
        tweets = []

        try:

            fetched_tweets = self.api.search(
                q=query, count=count, tweet_mode='extended')

            # parsing tweets one by one
            for tweet in fetched_tweets:
                # empty dictionary to store required params of a tweet
                parsed_tweet = {}

                # tweet_text = len(tweet.retweeted_status.full_text) > len(tweet.full_text) ? tweet.retweeted_status.full_text : tweet.full_text
                # saving text of tweet
                parsed_tweet['text'] = tweet.full_text
                # saving sentiment of tweet
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(
                    tweet.full_text)

                # appending parsed tweet to tweets list
                if tweet.retweet_count > 0:
                    # if tweet has retweets, ensure that it is appended only once
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)

            return tweets

        except tweepy.TweepError as e:
            # print error (if any)
            print("Error : " + str(e))

    def get_raw_tweets(self, query, count=10):
        ''' 
        Main function to fetch tweets and parse them. 
        '''
        # empty list to store parsed tweets
        tweets = []

        try:

            fetched_tweets = self.api.search(
                q=query, count=count, tweet_mode='extended')

            # parsing tweets one by one
            for tweet in fetched_tweets:
               
                if tweet.retweet_count > 0:
                    # if tweet has retweets, ensure that it is appended only once
                    if tweet not in tweets:
                        tweets.append(self.clean_tweet(tweet.full_text))
                else:
                    tweets.append(self.clean_tweet(tweet.full_text))

            return tweets

        except tweepy.TweepError as e:
            # print error (if any)
            print("Error : " + str(e))
