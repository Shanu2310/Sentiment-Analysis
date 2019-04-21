classifier = []
for tweet in tweets:
    if tweet.sentiment != "neutral":
        classifier_tuple = ()
        classifier_tuple.append(tweet.text)
        classifier_tuple.append(tweet.sentiment)
        classifier.append(classifier_tuple)    
