from src.SentimentAnalysis import TwitterClient
import yaml
from os import path as path


def get_twitter_keys():
    with open( path.join( path.abspath('.'), 'twitter-secret-keys.yaml' ), 'r') as stream:
        try:
            entries = yaml.load_all(stream)
            for entry in entries:
                print(entry)
        except yaml.YAMLError as exc:
            print(exc)
                    
          
def main():
    # creating object of TwitterClient Class 
    get_twitter_keys()
    api = TwitterClient() 
    # calling function to get tweets 
    tweets = api.get_tweets(query = 'Donald Trump', count = 200) 
  
    # picking positive tweets from tweets 
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive'] 
    # percentage of positive tweets 
    print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets))) 
    # picking negative tweets from tweets 
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative'] 
    # percentage of negative tweets 
    print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets))) 
    # percentage of neutral tweets 
    print("Neutral tweets percentage: {} %".format(100*len((frozenset(tweets) - frozenset(ntweets)) - frozenset(ptweets))/len(tweets)))

    
  
    # printing first 5 positive tweets 
    print("\n\nPositive tweets:") 
    for tweet in ptweets[:10]: 
        print(tweet['text']) 
  
    # printing first 5 negative tweets 
    print("\n\nNegative tweets:") 
    for tweet in ntweets[:10]: 
        print(tweet['text'])

  
if __name__ == "__main__": 
    # calling main function 
    main() 