
# University of Michigan
# Coursera: Python 3 Programming Specialization
# Course 2: Python Functions, Files and Dictionaries
# Week 3: Functions and Tuples
# Assessment: Functions

# 1
# A function is written which takes an integer as input and
# returns the same integer

def int_return(numb):
    return numb

# 2
# A function is written which takes an integer as input and
# returns the sum of that integer with two added.

def add(numb):
    return numb + 2

# 3
# A function is written which takes a string as input and adds "Nice
# to meet you!" to the end of the argument given and returns that
# new string.

def change(str_par):
    return str_par + "Nice to meet you!"

# 4
# A function is written which takes a list of integers as input and
# returns the sum of those integers.

def accum(lst_int):
    accum_var = 0
    for item in lst_int:
        accum_var += item
    return accum_var

# 5
# A function is written which takes a list as its input. If the
# length of the list is greater than or equal to 5, "Longer
# than 5" is returned. If the length is less than 5, "Less
# than 5" is returned.

def length(lst):
    if len(lst) >= 5:
        return "Longer than 5"
    else:
        return "Less than 5"

# 6
# A function is written which takes a number as an input and returns
# the number divided by two.
# Another function calls the first function to divide its parameter
# by two and returns the sum of the return value of the first function
# and the number six.

def divide(num):
    return num / 2

def sum(num):
    return divide(num) + 6
