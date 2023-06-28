
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

# 4
# A hidden class Student is supposed to accept two arguments in its
# constructor:
# A name string and an optional integer representing the number
# of years the student has been at Michigan (default:1)
#
# Every student has three instance variables:
# self.name (set to the name provided)
# self.years_UM (set to the number of years the student has been at
# Michigan)
# self.knowledge (initialized to 0)
#
# There are three methods:
# .study() should increase self.knowledge by 1 and return None
# .getKnowledge() should return the value of self.knowledge
# .year_at_umich() should return the value of self.years_UM

# A space is given where test cases are written to determine what
# errors there are. This information is used to answer multiple
# choice questions as well.

import test
student_1 = Student("Max")
student_2 = Student("Ann", 5)

test.testEqual(student_1.name, "Max")
test.testEqual(student_2.name, "Ann")

test.testEqual(student_1.years_UM, 1)
test.testEqual(student_2.years_UM, 5)

test.testEqual(student_1.knowledge, 0)
test.testEqual(student_2.knowledge, 0)

test.testEqual(student_1.getKnowlegde(), 0)

student_1.study()
test.testEqual(student_1.study(), None)
test.testEqual(student_1.knowledge, 1)

test.testEqual(student_1.year_at_umich(), 1)
test.testEqual(student_2.year_at_umich(), 5)

# It is concluded that the following test cases fail for the
# student class because:
# The attributes/instance variables are not correctly assigned in
# the constructor.
# The method study does not increase self.knowledge

# 5
# The following test cases are passed fine:
# The method study does not return None
# The optional integer in the constructor is not optional
# The method year_at_umich does not return the value of
# self.years_UM

# 6
# There is also another issue with the getKnowledge method
# because it returns None when self.knowledge is 0, even though
# it returns the correct value when self.knowledge is non-zero.
