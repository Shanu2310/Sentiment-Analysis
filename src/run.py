import SentimentAnalysis as sa
import sys
from process_excel import save_data, del_last_results_file
from classifier import *
import nltk

def prepare_classifier_input(tweets_list):
    classifier_input = []
    for tweet in tweets_list:
        if tweet['sentiment'] != "neutral":
            classifier_tuple = (tweet['text'], tweet['sentiment'][:3])
            classifier_input.append(classifier_tuple)
    
    return classifier_input


def main():
    # Removing results file from last run
    del_last_results_file()
    # creating object of TwitterClient Class 
    api = sa.TwitterClient() 
    # calling function to get tweets 
    print("Enter search term")
    tweets = api.get_tweets(query = sys.stdin.read(), count = 1000) 
    # saving data to excel file
    save_data("Training Set", tweets)
    # Preparing input list for classifier
    classifier_input_list = prepare_classifier_input(tweets)
    # Training classifier with already fetched tweets
    # train_classifier(classifier_input_list)
    # Fetch classifier test data from twitter
    print("Enter search term for feeding tweets to test classifier: ")
    test_tweets = api.get_raw_tweets(query = sys.stdin.read(), count = 1000)
    # Testing classifier
    classifier_output_list = classify_data(test_tweets, classifier_input_list)
    save_data("Result Set", classifier_output_list)

    
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
    nltk.download('punkt')
    main()
    