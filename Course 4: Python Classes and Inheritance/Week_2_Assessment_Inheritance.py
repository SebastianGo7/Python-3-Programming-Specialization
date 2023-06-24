
# University of Michigan
# Coursera: Python 3 Programming Specialization
# Course 4: Python Classes and Inheritance
# Week 2: Inheritance
# Assessment: Inheritance

# 1
# A class Pokemon describes a Pokemon and
# its leveling and evolving characteristics. An instance of the
# class is one pokemon is created.
#
# A subclass that inherits from Pokemon but changes
# some aspects, for instance, the boost values are different is
# called Grass_Pokemon.
#
# Another method called action that returns the string "[name of
# pokemon] knows a lot of different moves!". is added for the
# subclass Grass_Pokemon. An instance of this class with the name
# as "Belle" is created and this instance is assigned to the variable
# p1.

class Pokemon(object):
    attack = 12
    defense = 10
    health = 15
    p_type = "Normal"

    def __init__(self, name, level=5):
        self.name = name
        self.level = level

    def train(self):
        self.update()
        self.attack_up()
        self.defense_up()
        self.health_up()
        self.level = self.level + 1
        if self.level % self.evolve == 0:
            return self.level, "Evolved!"
        else:
            return self.level

    def attack_up(self):
        self.attack = self.attack + self.attack_boost
        return self.attack

    def defense_up(self):
        self.defense = self.defense + self.defense_boost
        return self.defense

    def health_up(self):
        self.health = self.health + self.health_boost
        return self.health

    def update(self):
        self.health_boost = 5
        self.attack_boost = 3
        self.defense_boost = 2
        self.evolve = 10

    def __str__(self):
        self.update()
        return "Pokemon name: {}, Type: {}, Level: {}".format(
            self.name, self.p_type, self.level)

class Grass_Pokemon(Pokemon):
    attack = 15
    defense = 14
    health = 12

    def update(self):
        self.health_boost = 6
        self.attack_boost = 2
        self.defense_boost = 3
        self.evolve = 12

    def moves(self):
        self.p_moves = ["razor leaf", "synthesis", "petal dance"]

    def action(self):
        return "{} knows a lot of different moves!".format(self.name)

p1 = Grass_Pokemon("Belle")

# 2
# The Grass_Pokemon subclass is modified so that the attack strength
# for its instances does not change until they reach level 10.
# At level 10 and up, their attack strength increases by the
# attack_boost amount when they are trained.
#
# An instance of the Grass_Pokemon class with the name as "Bulby" is
# created
# to test.
# The instance is assigned to the variable p2.
# Another instance of that class Grass_Pokemon with the name set to
# "Pika" is created and that instance is assigned to the variable p3.
# Then, Grass_Pokemon methods are used to train the p3 Grass_Pokemon
# instance until it reaches at least level 10.

class Pokemon(object):
    attack = 12
    defense = 10
    health = 15
    p_type = "Normal"

    def __init__(self, name, level=5):
        self.name = name
        self.level = level

    def train(self):
        self.update()
        self.attack_up()
        self.defense_up()
        self.health_up()
        self.level = self.level + 1
        if self.level % self.evolve == 0:
            return self.level, "Evolved!"
        else:
            return self.level

    def attack_up(self):
        self.attack = self.attack + self.attack_boost
        return self.attack

    def defense_up(self):
        self.defense = self.defense + self.defense_boost
        return self.defense

    def health_up(self):
        self.health = self.health + self.health_boost
        return self.health

    def update(self):
        self.health_boost = 5
        self.attack_boost = 3
        self.defense_boost = 2
        self.evolve = 10

    def __str__(self):
        return "Pokemon name: {}, Type: {}, Level: {}".format(
            self.name, self.p_type, self.level)

class Grass_Pokemon(Pokemon):
    attack = 15
    defense = 14
    health = 12
    p_type = "Grass"

    def update(self):
        self.health_boost = 6
        self.attack_boost = 2
        self.defense_boost = 3
        self.evolve = 12

    def moves(self):
        self.p_moves = ["razor leaf", "synthesis", "petal dance"]

    def attack_up(self):
        if self.attack < 10:
            return self.attack
        else:
            self.attack = self.attack + self.attack_boost
            return self.attack

p2 = Grass_Pokemon("Bulby")
p3 = Grass_Pokemon("Pika")
p2.update()
p2.attack_up()
print(p2.attack_up())
p3.update()
p3.attack_up()
