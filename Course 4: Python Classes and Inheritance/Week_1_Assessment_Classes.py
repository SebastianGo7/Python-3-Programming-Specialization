
# University of Michigan
# Coursera: Python 3 Programming Specialization
# Course 4: Python Classes and Inheritance
# Week 1: Classes
# Assessment: Classes

# 1
# A class called Bike is defined which accepts a string and a float as
# input, and those inputs are assigned respectively to two instance
# variables, color and price. To the variable testOne an instance of
# Bike whose color is blue and whose price is 89.99 is assigned.
# To the variable testTwo an instance of Bike whose color is
# purple and whose price is 25.0 is assigned.

class Bike:
    def __init__(self, init_color, init_price):
        self.color = init_color
        self.price = init_price
testOne = Bike("blue", 89.99)
testTwo = Bike("purple", 25.0)

# 2
# A class called AppleBasket whose constructor accepts two
# inputs: a string representing a color, and a number representing a
# quantity of apples is created. Two instance variables:
# apple_color and apple_quantity are initialized by the constructor.
# A class method called increase is written that increases the
# quantity by 1 each time it is invoked.
# A __str__ method for this class is written which returns a string
# of the format: "A basket of [quantity goes
# here] [color goes here] apples." e.g. "A basket of 4 red apples."
# or "A basket of 50 blue apples."

class AppleBasket():
    def __init__(self, init_color, init_quantity):
        self.apple_color = init_color
        self.apple_quantity = init_quantity

    def increase(self):
        self.apple_quantity += 1

    def __str__(self):
        return "A basket of {} {} apples.".format(self.apple_quantity,
                                                  self.apple_color)
basket_1 = AppleBasket("yellow", 32)
print(basket_1)
