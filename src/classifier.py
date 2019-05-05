from textblob.classifiers import NaiveBayesClassifier

def train_classifier(classifier_input):
    return NaiveBayesClassifier(classifier_input)


def classify_data(test_tweets, train_tweets):
    classifier = train_classifier(train_tweets)
    classified_data = []
    for entry in test_tweets:
        sentiment = classifier.classify(entry)

        result = {}
        result['text'] = entry
        result['sentiment'] = sentiment

        classified_data.append(result)

    return classified_data