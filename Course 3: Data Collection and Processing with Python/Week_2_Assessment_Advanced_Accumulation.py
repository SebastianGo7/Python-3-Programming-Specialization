
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

# 5
# A list of tuples with students' names and scores is given. List
# comprehension is used to create a new list passed that contains
# the names of students who passed the class (had a final grade of
# 70 or greater).

students = [('Tommy', 95), ('Linda', 63), ('Carl', 70), ('Bob', 100),
            ('Raymond', 50), ('Sue', 75)]
passed = [name[0] for name in students if name[1] >= 70]

# 6
# Zip and filter is used so that these lists (l1 and l2)
# are combined into one big list and assigned to the variable
# opposites if they are both longer than 3 characters each.

l1 = ['left', 'up', 'front']
l2 = ['right', 'down', 'back']

opposites = list(
    filter(lambda value: (len(value[0]) > 3 and len(value[1])),
           zip(l1, l2)))

# 7
# A species list and a population list is provided. Zip is used to
# combine these lists into one list of tuples called pop_info.
# From this list, a new list is created called endangered that
# contains the names of species whose populations are below 2500.

species = ['golden retriever', 'white tailed deer', 'black rhino',
           'brown squirrel', 'field mouse', 'orangutan',
           'sumatran elephant', 'rainbow trout', 'black bear',
           'blue whale', 'water moccasin', 'giant panda',
           'green turtle', 'blue jay', 'japanese beetle']

population = [10000, 90000, 1000, 2000000, 500000, 500, 1200, 8000,
              12000, 2300, 7500, 100, 1800, 9500, 125000]
pop_info = list(zip(species, population))
endangered = [(x1) for (x1, x2) in list(zip(species, population)) if
              (int(x2) < 2500)]

