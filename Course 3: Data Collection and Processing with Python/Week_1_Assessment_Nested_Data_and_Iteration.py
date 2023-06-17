
# University of Michigan
# Coursera: Python 3 Programming Specialization
# Course 3: Data Collection and Processing with Python
# Week 1: Nested Data and Iteration
# Assessment: Nested Data and Iteration

# 1
# A nested list is given. a specific value of the dictionary is
# assigned to a variable using indexing.

nesteddict = [['dog', 'cat', 'horse'],
          ['frog', 'turtle', 'snake', 'gecko'],
          ['hamster', 'gerbil', 'rat', 'ferret']]
output = nesteddict[1][2]

# 2
# In and not in tests are used to create Boolean values with given
# lists.

lst = [['apple', 'orange', 'banana'], [5, 6, 7, 8, 9.9, 10],
       ['green', 'yellow', 'purple', 'red']]

# It is tested if yellow is in the third list of lst
for item in lst[2]:
    if "yellow" in item:
        yellow = True

# It is tested if 4 is the second list of lst.
for number in lst[1]:
    if number == 4:
        four = True
    else:
        four = False

# It is tested if 'orange' is the first element of lst.
for colour in lst[0]:
    if 'orange' in colour:
        orange = True

# 3
# Statements are used to create Boolean values with given
# lists according to instructions.

L = [[5, 8, 7], ['hello', 'hi', 'hola'], [6.6, 1.54, 3.99],
     ['small', 'large']]

# It is tested if 'hola' is in the list L
for item in L:
    if item == "hola":
        test1 = True
    else:
        test1 = False

# It is tested if [5, 8, 7] is in the list L
for item in L:
    if item == [5, 8, 7]:
        test2 = True
        break
    else:
        test2 = False

# It is tested if 6.6 is the third element of the list L.
for item in L:
    for sublist in item:
        if type(sublist) == float:
            if float(sublist) == 6.6:

                test3 = True
                break
            else:
                test3 = False

# 4
# A nested data structure is given to follow instructions to examine
# it.
nesteddict = {'data': ['finding', 23, ['exercises', 'hangout', 34]],
          'window': ['part', 'whole', [], 'sum',
                     ['math', 'calculus', 'algebra', 'geometry',
                      'statistics',
                      ['physics', 'chemistry', 'biology']]]}

# It is checked if the string 'data' is a key in nested.
data = bool
for part in nesteddict:
    if part == "data":
        data = True
        break
    else:
        data = False

# It is checked if the integer 24 is in the value of the key data.

for item in nesteddict:
    if item == "window":
        for sublist in nesteddict["window"]:
            if sublist == "whole":
                whole = False
                break
            else:
                whole = True

# It is checked that the string 'whole' is not in the value of the
# key window.

for item in nesteddict['data']:
    if type(item) == int:
        if item == 24:
            twentyfour = True
        else:
            twentyfour = False

# It is checked if the string 'physics' is a key in the dictionary
# nested.

physics = bool

for item in nesteddict:
    for sublist in nesteddict[item]:
        if type(sublist) == list:
            for subsublist in sublist:
                if type(subsublist) == list:
                    for subsubsubitem in subsublist:
                        print(subsubsubitem)
                        for subsubsubsubitem in subsubsubitem:
                            if subsubsubsubitem == "physics":
                                physics = True
                                break
                            else:
                                physics = False

