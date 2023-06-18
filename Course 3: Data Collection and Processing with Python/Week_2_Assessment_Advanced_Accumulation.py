
# University of Michigan
# Coursera: Python 3 Programming Specialization
# Course 3: Data Collection and Processing with Python
# Week 2: Map, Filter and List Comprehensions
# Assessment: Advanced Accumulation

# 1
# All the elements in lst_check are assigned to the variable
# map_testing with the string "Fruit: " added to it using the map
# function.
lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries',
             'blueberries', 'peaches', 'apples', 'mangos', 'papaya']

map_testing = list(map(lambda value: "Fruit: " + value, lst_check))

# 2
# Filter is used to produce a list called b_countries that only
# contains the strings from the given countries list that begin with B.

countries = ['Canada', 'Mexico', 'Brazil', 'Chile', 'Denmark',
             'Botswana', 'Spain', 'Britain', 'Portugal', 'Russia',
             'Thailand', 'Bangladesh', 'Nigeria', 'Argentina',
             'Belarus', 'Laos', 'Australia', 'Panama', 'Egypt',
             'Morocco', 'Switzerland', 'Belgium']
b_countries = list(filter(lambda count: count[0] == "B", countries))

# 3
# Using list comprehension, a list of strings called first_names
# that contains only the first names of everyone of an given people
# list is created.

people = [('Snow', 'Jon'), ('Lannister', 'Cersei'), ('Stark', 'Arya'),
          ('Stark', 'Robb'), ('Lannister', 'Jamie'),
          ('Targaryen', 'Daenerys'), ('Stark', 'Sansa'),
          ('Tyrell', 'Margaery'), ('Stark', 'Eddard'),
          ('Lannister', 'Tyrion'), ('Baratheon', 'Joffrey'),
          ('Bolton', 'Ramsey'), ('Baelish', 'Peter')]

first_names = [value[1] for value in people]

# 4
#
# List comprehension is used to create a list called lst2 that doubles
# each element in the list, lst.
lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]
lst2 = [value * 2 for value in lst]

