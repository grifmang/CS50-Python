import nltk
from nltk.tokenize import TweetTokenizer
import os
import sys

tokens = TweetTokenizer()

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""

        # Initialize positives and negatives
        self.positives = os.path.join(sys.path[0], "positive-words.txt")
        self.negatives = os.path.join(sys.path[0], "negative-words.txt")
        
    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
        
        self.text = text
        token_result = []
        result = 0
        pos_file = open(self.positives, encoding='utf-8')
        neg_file = open(self.negatives, encoding='utf-8')
        pos_string = pos_file.read() 
        neg_string = neg_file.read()
        pos_string = pos_string.split()
        neg_string = neg_string.split()
        
        
        token = tokens.tokenize(text)
        #Perfect up to here. token is split list.
        
        # Calculate sentiment score
        for word in token:
            for line in pos_string:
                if word == line:
                    result += 1
            for element in neg_string:
                if word == element:
                    result -= 1
            
            
        pos_file.close()
        neg_file.close()
        #helpers.chart(positive, negative, neutral)
        return int(result)