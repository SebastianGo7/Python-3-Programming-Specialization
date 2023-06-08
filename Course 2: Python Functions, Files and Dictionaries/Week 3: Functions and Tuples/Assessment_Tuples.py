
# University of Michigan
# Coursera: Python 3 Programming Specialization
# Course 2: Python Functions, Files and Dictionaries
# Week 3: Functions and Tuples
# Assessment: Tuples

# 1
# A tuple is created which includes the given information.

olympics = "Beijing", "London", "Rio", "Tokyo"

# 2
# A list of the second elements of a given tuple is created.

tuples_lst = [('Beijing', 'China', 2008), ('London', 'England', 2012),
              ('Rio', 'Brazil', 2016, 'Current'),
              ('Tokyo', 'Japan', 2020, 'Future')]
country = []

for item in tuples_lst:
    country.append(item[1])

print(country)

# 3
# The values of a given tuple are assigned to given variables in one
# line of code.

olymp = ('Rio', 'Brazil', 2016)
city, country, year = olymp

# 4
# A function is defined which calls five given parameters and
# returns a tuple of those values in that order.
#
# Define a function called info with five parameters: name, gender,
# age, bday_month, and hometown. The function should then return a
# tuple with all five parameters in that order.

def info(name, gender, age, bday_month, hometown):
    return name, gender, age, bday_month, hometown

# 5
# A list is created which contains the values of a given dictionary
# without using the .keys() method.

gold = {'USA': 31, 'Great Britain': 19, 'China': 19, 'Germany': 13,
        'Russia': 12, 'Japan': 10, 'France': 8, 'Italy': 8}
num_medals = []

for item in gold.items():
    num_medals.append(item[1])
    print(item)
