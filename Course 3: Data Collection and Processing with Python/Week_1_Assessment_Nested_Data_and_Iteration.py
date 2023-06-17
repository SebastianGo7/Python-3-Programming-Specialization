
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

# 5
# A nested dictionary is given. The value is fetched using indexing.

nested_d = {'Beijing': {'China': 51, 'USA': 36, 'Russia': 22,
                        'Great Britain': 19},
            'London': {'USA': 46, 'China': 38, 'Great Britain': 29,
                       'Russia': 22},
            'Rio': {'USA': 35, 'Great Britain': 22, 'China': 20,
                    'Germany': 13}}
london_gold = 0
for olympic in nested_d:
    if olympic == "London":
        for country in nested_d[olympic]:
            if country == "Great Britain":
                london_gold += nested_d[olympic][country]

# 6
# A nested dictionary is provided, to fetch specific variables using
# indexing according to further instructions.
sports = {'swimming': ['butterfly', 'breaststroke', 'backstroke',
                       'freestyle'],
          'diving': ['springboard', 'platform', 'synchronized'],
          'track': ['sprint', 'distance', 'jumps', 'throws'],
          'gymnastics': {'women': ['vault', 'floor', 'uneven bars',
                                   'balance beam'],
                         'men': ['vault', 'parallel bars', 'floor',
                                 'rings']}}

# The string 'backstroke' is assigned to the name v1
v1 = sports['swimming'][2]
# The string 'platform' is assigned to the name v2
v2 = sports['diving'][1]
# The list ['vault', 'floor', 'uneven bars', 'balance beam']
# is assigned to the name v3
v3 = sports['gymnastics']['women']
# The string 'rings' is assigned  to the name v4
v4 = sports['gymnastics']['men'][3]

# 7
# A specific values of a dictionary are fetched and appended to a list.

nested_d = {'Beijing': {'China': 51, 'USA': 36, 'Russia': 22,
                        'Great Britain': 19},
            'London': {'USA': 46, 'China': 38, 'Great Britain': 29,
                       'Russia': 22},
            'Rio': {'USA': 35, 'Great Britain': 22, 'China': 20,
                    'Germany': 13}}

US_count = []

for item in nested_d:
    for sublist in nested_d[item]:
        if sublist == "USA":
            US_count.append(nested_d[item][sublist])
        print(nested_d[item][sublist])

# 8
# The third element of the contents of l_of_l of the sublists are
# assigned to the list third.
l_of_l = [['purple', 'mauve', 'blue'],
          ['red', 'maroon', 'blood orange', 'crimson'],
          ['sea green', 'cornflower', 'lavender', 'indigo'],
          ['yellow', 'amarillo', 'mac n cheese', 'golden rod']]
third = []
for item in l_of_l:
    third.append(item[2])
