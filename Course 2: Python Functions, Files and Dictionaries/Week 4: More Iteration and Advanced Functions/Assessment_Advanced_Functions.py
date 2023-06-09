
# University of Michigan
# Coursera: Python 3 Programming Specialization
# Course 2: Python Functions, Files and Dictionaries
# Week 4: More about Iteration and Advanced Functions
# Assessment: Advanced_Functions

# 1
# A function is defined which has one parameter which should be an
# integer, and one optional parameter that can either be a number or
# a string and whose default is 6. The function returns the
# multiplication of the first and second parameter.

def mult(par_int, par_item=6):
    return par_int * par_item

# 2
# A given function with an error does not work and is fixed by
# changing the definition of the function.
# The function concatenates given strings.

def greeting(name, greeting="Hello ", excl="!"):
    return greeting + name + excl

print(greeting("Bob"))
print(greeting(""))
print(greeting("Bob", excl="!!!"))

# 3
# A given function with an error does not work and is fixed by
# changing the definition of the function.
# The function sums up the parameters' values.

def sum(intx, intz=5):
    return intz + intx

# 4
# A function is written which takes three parameters, a required
# integer, an optional boolean whose default value is True, and an
# optional dictionary, called dict1, whose default value is
# {2:3, 4:5, 6:8}. If the boolean parameter is False, the boolean
# value "False"is returned. If the boolean parameter True,
# it is tested if the integer is a key is in the dictionary. The
# value of that integer is returned then.

def test(par_int, par_bool=True, dict1={2: 3, 4: 5, 6: 8}):
    if par_bool == True:
        if par_int in dict1.keys():
            return dict1[par_int]
    else:
        return False

# 5
# A function is written which takes three parameters. One required
# parameter which should be a string, a second optional parameter
# whose default value is True. And a third optional parameter called
# d that has the default value of {'apple': 2, 'pear': 1, 'fruit': 19,
# 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}.
# The function checks to see if the first parameter is a key in the
# third parameter if the second parameter is true. If it as True is
# returned otherwise False is returned.
# The function checks if the first parameter is not a key in the
# third if the second parameter is False. If it is not, True is
# returned and if it is False is returned.

def checkingIfIn(par_str, direction=True,
                 d={'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5,
                    'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if direction == True:
        if par_str in d.keys():
            return True
        else:
            return False
    else:
        if par_str not in d.keys():
            return True
        else:
            return False

# 6
# A function is provided which checks if the first parameter is in
# the dictionary parameter, and if it is it returns the value. If
# not it returns False. Specific variables assignments should be
# created according to descriptions.

def checkingIfIn(a, direction=True,
                 d={'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5,
                    'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if direction == True:
        if a in d:
            return d[a]
        else:
            return False
    else:
        if a not in d:
            return True
        else:
            return d[a]

# The function is called with parameters to return false
c_false = checkingIfIn(14)

# The function is called with parameters to return true
c_true = checkingIfIn(15, direction=False)

# The function is called with parameters to return the value of fruit
fruit_ans = checkingIfIn('fruit')

# The function is called with parameters to return 8
param_check = checkingIfIn(8, direction=True, d={8: 8})
