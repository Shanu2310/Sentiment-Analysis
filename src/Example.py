# to create data for naive bayes classifier
classifier_input = []
for tweet in tweets:
    if tweet['sentiment'] != "neutral":
        classifier_tuple = (tweet['text'], tweet['sentiment'])