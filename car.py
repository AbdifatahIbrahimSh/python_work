"""A set of classes used to represent gas and elecric cars"""

class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """Initialize attritubes of the car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """"Retuns the descriptive name of the car"""
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()

    def read_odometer(self):
        """Showing car odometer"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """updates the mileage of the car"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else: 
            print("you cannot roll back an adometer")

    def increment_odometer(self, miles):
        """Increment the value of the odometer"""
        if miles >= 0:
            self.odometer_reading += miles
        else: 
            print("you can't roll back an odometer")

    def fill_gas_tank(self):
        """Tells if the tanks is empty or full"""
        print(f"This car has a full tank")



    