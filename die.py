"""A class represent a Die"""

from random import randint

class Die:
    """Represents a die"""

    def __init__(self, sides):
        """initializes a die object"""
        self.sides = sides

    def roll_die(self, times=1):
        for number in range(1, times):
            random_number = randint(1, self.sides)
            print(random_number, end=' ')


first_die = Die(6)
second_die = Die(10)
third_die = Die(20)

first_die.roll_die(10)
print()
second_die.roll_die(10)
print()
third_die.roll_die(10)