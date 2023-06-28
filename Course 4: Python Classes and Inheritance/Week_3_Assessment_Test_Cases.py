
# University of Michigan
# Coursera: Python 3 Programming Specialization
# Course 4: Python Classes and Inheritance
# Week 3: Test Cases
# Assessment: Test Cases

# 1
# A hidden function mySum is given which is supposed to return
# the sum of a list of numbers (and 0 if that list is empty),
# but it has one or more errors in it.
# A space is given where test cases are written to determine what
# errors there are. This information is used to answer multiple
# choice questions as well.

import test
test.testEqual(mySum([]), 0)
test.testEqual(mySum([5]), 5)
test.testEqual(mySum([5, 2, 2]), 9)

# 2
# It is concluded that the following test cases fail for the mySum
# function: An empty list, a list with more then one item.
# (A list with one item works fine)

# 3
# It is also concluded, that at the moment its not possible to
# tell if other cases would fail (such as combining integers and
# floats). These cases can be tested if the current issues are
# fixed.
