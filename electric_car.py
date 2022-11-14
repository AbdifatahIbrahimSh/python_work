"""A set of classes used to represent elecric cars"""

from car import Car

class Battery:
    """A simple model for battery of an elecric car"""

    def __init__(self, battery_size=75):
        """initializes the battery object of an elecric car """
        self.battery_size = battery_size

    def describe_battery(self):
        """Prints the full description of the car battery"""
        print(f"This car has a {self.battery_size}-kwh battery")

    def get_range(self):
        """Prints a statement about the range of this battery"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"this car has a {range} miles on a full charge.")


class ElectricCar(Car):
    """A simple attempt to represent an elecric car"""

    def __init__(self, make, model, year):
        "Initialize the parent and child class"
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        """Overrides the fill_gas_tank of the gas car"""
        print("This car doesn't have a gas tank")
