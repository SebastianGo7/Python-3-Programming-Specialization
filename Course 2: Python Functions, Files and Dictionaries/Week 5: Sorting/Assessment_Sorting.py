
# University of Michigan
# Coursera: Python 3 Programming Specialization
# Course 2: Python Functions, Files and Dictionaries
# Week 5: Sorting
# Assessment: Sorting

# 1
# The given string is sorted from z to a and assigned to a variable.

letters = "alwnfiwaksuezlaeiajsdl"
sorted_letters = sorted(letters, reverse=True)

# 2
# The given list is sorted in alphabetical order and saved in a
# another list

animals = ['elephant', 'cat', 'moose', 'antelope', 'elk', 'rabbit',
           'zebra', 'yak', 'salamander', 'deer', 'otter', 'minx',
           'giraffe', 'goat', 'cow', 'tiger', 'bear']

animals_sorted = sorted(animals)

# 3
# The keys of a dictionary are saved in a list which is also sorted
# alphabetically

medals = {'Japan': 41, 'Russia': 56, 'South Korea': 21,
          'United States': 121, 'Germany': 42, 'China': 70}
alphabetical = sorted(medals)

# 4
# The keys of a dictionary are saved in a list which is also sorted
# by its values from lowest to highest. The three keys with the highest
# values are saved in a separate list as well.

medals = {'Japan': 41, 'Russia': 56, 'South Korea': 21,
          'United States': 121, 'Germany': 42, 'China': 70}
sorted_medals = sorted(medals, key=lambda k: medals[k], reverse=True)
print(sorted_medals)
top_three = []

for country in range(3):
    top_three.append(sorted_medals[country])
print(top_three)

# 5
# The keys of a dictionary are saved in a list which is also sorted
# by its values from highest to lowest.

groceries = {'apples': 5, 'pasta': 3, 'carrots': 12, 'orange juice': 2,
             'bananas': 8, 'popcorn': 1, 'salsa': 3, 'cereal': 4,
             'coffee': 5, 'granola bars': 15, 'onions': 7, 'rice': 1,
             'peanut butter': 2, 'spinach': 9}
most_needed = sorted(groceries, key=lambda k: groceries[k],
                     reverse=True)

# 6
# A function is written which takes a single integer and returns
# the last four digits to use it as a key of the sorted() function.
# The sorted function is used to sort a list of integers using the
# defined function as a sorting key function.

def last_four(x):
    last_four_lst = []
    extra_lst = []
    last_four_lst = str(x)

    extra_lst = last_four_lst[4:8]

    last_four_lst = int((("")).join(extra_lst))
    return last_four_lst

ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
sorted_ids = sorted(ids, key=last_four)

# 7
# A list of integers is sorted by its last four digits using a
# lambda function and the sorted function; the sorted result is
# saved in a another list.

ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]

sorted_id = sorted(ids, key=(lambda x: int(str(x)[4:8])))

# 8
# A list of strings is sorted by each elements letter a to z using
# the lambda function; saving the result in another list.

ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']

lambda_sort = sorted(ex_lst, key=(lambda text: text[1]))
print(lambda_sort)
