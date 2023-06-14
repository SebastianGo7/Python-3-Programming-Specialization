
# University of Michigan
# Coursera: Python 3 Programming Specialization
# Course 2: Python Functions, Files and Dictionaries
# Week 5: Sorting
# Final Course Project: Sentiment Classifier

# File and Papers of Sentiment Analysis
# http://www.cs.uic.edu/~liub/FBS/sentiment-analysis.html

# 1
# A synthetic (fake, semi-randomly generated) twitter data is given
# in a file named project_twitter_data.csv, which has the text of a
# tweet, the number of retweets of that tweets and the number of
# replies to that tweet.
# Words list that express positive and negative sentiment are also
# given through positive_words.txt and negative_words.txt.
# A sentiment classifier is created which detects how positive or
# negative each tweet is.
#
# A csv file is created, which contains columns for Number of
# Retweets, Number of Replies, Positive Score Positive Score (which
# is how many happy words are in the tweet), Negative Score (which
# is how many angry words are in the tweet), and the Net Score for
# each tweet. At the end, a graph of the Net Score vs Number of
# Retweets is created and uploaded through Google Sheets.

# A function called strip_punctuation is written, which takes one
# parameter,a string which represents a word, and removes characters
# considered punctuation from that string.

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(word_str):
    # Punctuation chars are removed 
    ret_word = ""
    for char in word_str:
        if char in punctuation_chars:
            word_str = word_str.replace(char, "")
    return word_str

# 2
# A function called get_pos is defined. It calculates how many words
# in the parameter string (which represents one or more sentences) are
# considered positive words. This is returned by a positive integer 
# indicating the occurrences of positive words using the previously 
# defined strip_punctuation function as well. 
# The list positive_words is used to determine which words count
# positive.
# Next, copy in your strip_punctuation function and define a
# function called get_pos which takes one parameter, a string which
# represents one or more sentences, and calculates how many words in
# the string are considered positive words. 

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

positive_words = []
with open("positive_words.txt") as pos_f:
    # Positive words are appended to a list.
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
        print(lin)

def strip_punctuation(word_str):
    # Punctuation chars are removed.
    ret_word = ""
    for char in word_str:
        if char in punctuation_chars:
            word_str = word_str.replace(char, "")
    return word_str

def get_pos(word_str):
    word_str = (strip_punctuation(word_str)).lower()
    # Words need to be converted to lower case, because all words in
    # the list positive_words are lower cased.
    
    word_lst = word_str.split()
    ret_lst = []
    accum = 0
    for word in word_lst:
        if word in positive_words:
            accum += 1
    return accum

print(positive_words)

# 3
# The function get_neg does the same as get_pos for negative words 
# from the negative_words.txt list.

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

negative_words = []
with open("negative_words.txt") as pos_f:
    # Negative words are appended to a list.
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def strip_punctuation(word_str):
    # Punctuation chars are removed. 
    ret_word = ""
    for char in word_str:
        if char in punctuation_chars:
            word_str = word_str.replace(char, "")
    return word_str
            
def get_neg(word_str):
    word_str = (strip_punctuation(word_str)).lower()
    # Words need to be converted to lower case, because all words in
    # the list negative_words are lower cased.
    word_lst = word_str.split()
    ret_lst = []
    accum = 0
    for word in word_lst:
        if word in negative_words:
            accum += 1
    return accum
