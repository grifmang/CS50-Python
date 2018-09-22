from flask import Flask, redirect, render_template, request, url_for
import os, sys
import helpers
from analyzer import Analyzer
from nltk.tokenize import TweetTokenizer
tokens = TweetTokenizer()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():
    
    positive = 0.0
    negative = 0.0
    neutral = 0.0
    
    # Initialize positives and negatives
    positives = os.path.join(sys.path[0], "positive-words.txt")
    negatives = os.path.join(sys.path[0], "negative-words.txt")
        

    # validate screen_name
    screen_name = request.args.get("screen_name", "").lstrip("@")
    if not screen_name:
        return redirect(url_for("index"))

    # get screen_name's tweets
    tweets = helpers.get_user_timeline(screen_name)

    # TODO
    result_dict = {}
    token_result = []
    result = 0
    pos_file = open(positives, encoding='utf-8')
    neg_file = open(negatives, encoding='utf-8')
    pos_string = pos_file.read() 
    neg_string = neg_file.read()
    pos_string = pos_string.split()
    neg_string = neg_string.split()
    
    for tweet in tweets:
        result_dict[tweet] = 0
        
    for element, values in result_dict.items():
        element = element.lower()
        token = tokens.tokenize(element)
        for word in token:
            for line in pos_string:
                if word == line:
                    positive += 1
            for element in neg_string:
                if word == element:
                    negative += 1
            
            neutral += 1
            
    pos_file.close()
    neg_file.close()
        
    # generate chart
    chart = helpers.chart(positive, negative, neutral)

    # render results
    return render_template("search.html", chart=chart, screen_name=screen_name)
