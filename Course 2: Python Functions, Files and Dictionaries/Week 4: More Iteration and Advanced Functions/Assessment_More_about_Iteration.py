      
# University of Michigan
# Coursera: Python 3 Programming Specialization
# Course 2: Python Functions, Files and Dictionaries
# Week 4: More about Iteration and Advanced Functions
# Assessment: More about Iteration

# 1
# A function is defined which takes a list of numbers as the
# parameter and returns a sublist. The sublist contains all values
# of the original list until it reaches the number 5.

def sublist(lst_numbers):
    counter = 0
    ret_list = []
    while lst_numbers[counter] != 5:
        # List values are appended until the number 5 is found.
        ret_list.append(lst_numbers[counter])
        counter += 1
        if counter == len(lst_numbers):
            break
    return ret_list

# 2
# A function is defined which takes a list of numbers as the
# parameter and returns a sublist. The sublist contains all values
# of the original list until it reaches the number 7.

def check_nums(par_lst):
    counter = 0
    ret_lst = []
    while par_lst[counter] != 7:
        # List values are appended until the number 7 is found.
        ret_lst.append(par_lst[counter])
        counter += 1
        if counter == len(par_lst):
            break
    return ret_lst

# 3
# A function is defined which takes a list of strings as the
# parameter and returns a sublist. The sublist contains all values
# of the original list until it reaches the string "STOP".
#

def sublist(par_lst):
    counter = 0
    ret_lst = []
    while par_lst[counter] != "STOP":
        # List values are appended until "STOP" is found.
        ret_lst.append(par_lst[counter])
        counter += 1
        if counter == len(par_lst):
            break
    return ret_lst

# 4
# A function is defined which takes a list of strings as the
# parameter and returns a sublist. The sublist contains all values
# of the original list until it reaches the string "z".

def stop_at_z(par_lst):
    counter = 0
    ret_lst = []
    while par_lst[counter] != "z":
        # List values are appended until "z" is found.
        ret_lst.append(par_lst[counter])
        counter += 1
        if counter == len(par_lst):
            break
    return ret_lst

# 5
# A while loop is defined which does the same as a given for loop.
# The accumulated sum of the values of the list is calculated.

lst = [65, 78, 21, 33]
counter = 0
sum2 = 0
while counter < len(lst):
    # the actual value is added to the current sum
    sum2 += lst[counter]
    counter += 1

sum1 = 0
for x in lst:
    sum1 = sum1 + x

# 6
# A function is defined which takes a list as input, includes a
# while loop that stops when the string "bye" is found.
# A list that contains the first 10 strings is returned, regardless
# of where the loop stops. (i.e., the first ten are returned if it
# finds "bye"on the 32nd element; the first 4 are returned if it
# finds "bye" on the 5th element.) Slicing shall not be used.

def beginning(par_lst):
    counter = 0
    lst_ret = []
    while par_lst[counter] != "bye":
        # The actual value is appended until "bye" is reached or ten
        # strings have been appended already.
        lst_ret.append(par_lst[counter])
        counter += 1
        if counter == 10:
            break
    return lst_ret

