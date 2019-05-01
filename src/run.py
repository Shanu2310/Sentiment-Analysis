import SentimentAnalysis as sa
import sys
from process_excel import *


def prepare_classifier_input(tweets_list):
    classifier_input = []
    for tweet in tweets_list:
        if tweet['sentiment'] != "neutral":
            classifier_tuple = (tweet['text'], tweet['sentiment'][:3])
            classifier_input.append(classifier_tuple)
    
    return classifier_input


def main():
    # creating object of TwitterClient Class 
    api = sa.TwitterClient() 
    # calling function to get tweets 
    print("Enter search term")
    tweets = api.get_tweets(query = sys.stdin.read(), count = 1000) 
    # saving data to excel file
    save_data("Training Set", tweets)
    # Preparing input list for classifier
    classifier_input_list = prepare_classifier_input(tweets)
  
    # picking positive tweets from tweets 
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive'] 
    # percentage of positive tweets 
    pos_tweet_percentage = 100*len(ptweets)/len(tweets)
    print("Positive tweets percentage: {} %".format(pos_tweet_percentage)) 
    # picking negative tweets from tweets 
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative'] 
    # percentage of negative tweets 
    neg_tweet_percentage = 100*len(ntweets)/len(tweets)
    print("Negative tweets percentage: {} %".format(neg_tweet_percentage)) 
    # percentage of neutral tweets 
    print("Neutral tweets percentage: {} %".format(100 - pos_tweet_percentage - neg_tweet_percentage))

    
  
    # printing first 10 positive tweets 
    print("\nPositive tweets: ") 
    for tweet in ptweets[:10]: 
        print(tweet['text']) 
  
    # printing first 10 negative tweets 
    print("\n\nNegative tweets:") 
    for tweet in ntweets[:10]: 
        print(tweet['text'])

  
if __name__ == "__main__": 
    # calling main function 
    main()
    