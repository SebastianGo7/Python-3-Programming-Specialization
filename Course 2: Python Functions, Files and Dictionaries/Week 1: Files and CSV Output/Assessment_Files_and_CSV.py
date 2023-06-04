
# University of Michigan
# Coursera: Python 3 Programming Specialization
# Course 2: Python Functions, Files and Dictionaries
# Week 1: Chapter Files and CSV Output
# Assessment: Files and CSV

# 1
# Text file travel_plans.txt is opened and
# total number of characters is saved.

num = 0
with open("travel_plans.txt", 'r') as file_travelplans:

    text = file_travelplans.read()
    num = len(text)

# 2
# Text file emotion_words.txt is opened which include lines of words
# and total number of words is assigned to a variable.

num_words = 0
lst_words = 0
with open("emotion_words.txt", 'r') as file_emotions:
    text = file_emotions.read()
    lst_words = text.split()
    num_words = len(lst_words)

# 3
# Text file school_prompt.txt is opened which includes lines of words
# and total number of lines are assigned to a variable.

num_lines = 0
with open("school_prompt.txt", 'r') as file_school:
    lst_text = file_school.readlines()
    num_lines = len(lst_text)

# 4
# Text file school_prompt.txt which is a string is opened and
# first 30 characters are assigned to a variable.

beginning_chars = ""
with open("school_prompt.txt", 'r') as file_school:
    text = file_school.read()
    for numb in range(30):
        beginning_chars += str(text[numb])

# 5
# Text file school_prompt.txt which is a string is opened and
# every third word of every line is appended to a list.
three = []

with open("school_prompt.txt", 'r') as file_school:
    text = file_school.readlines()
    for aline in text:
        lst_words = aline.split()
        three.append(lst_words[2])
print(three)

# 6
# Text file emotion_words.txt is opened and
# every first word of a line is appended to a list.

emotions = []
with open("emotion_words.txt", 'r') as file_emotions:
    lst_text = file_emotions.readlines()
    for aline in lst_text:
        lst_words = aline.split()
        emotions.append(lst_words[0])
print(emotions)

# 7
# Text file emotion_words.txt is opened and
# the first 33 characters are assigned to a string variable

first_chars = ""
with open("travel_plans.txt", 'r') as file_travel:
    text = file_travel.read()
    for char in range(33):
        first_chars += str(text[char])

# 8
# Text file school_prompt.txt is opened and
# if the character 'p' is in a word it is appended to a list.

p_words = []
with open("school_prompt.txt", 'r') as file_school:
    text_lst = file_school.read().split()
    for word in text_lst:
        if "p" in word:
            p_words.append(word)
print(text_lst)

