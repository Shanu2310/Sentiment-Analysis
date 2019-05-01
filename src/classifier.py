from textblob.classifiers import NaiveBayesClassifier

def train_classifier(classifier_input):
    cl = NaiveBayesClassifier(classifier_input)
    