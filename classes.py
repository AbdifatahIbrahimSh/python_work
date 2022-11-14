from car import Car
from electric_car import ElectricCar
from user import User

# Inistansiation of user object
my_user = User('abdifatah', 'ibrahim')
your_user = User('hoodo', 'faysal')

your_user.describe_user()
your_user.greet_user()

print()

my_user.describe_user()
my_user.greet_user()

print()

# initialization of the gas car
my_car = Car('Audi', 'a4', 2003)
print(my_car.get_descriptive_name())
my_car.fill_gas_tank()
my_car.update_odometer(450)
my_car.read_odometer()

print()

# initialization of the elecric car
e_car = ElectricCar('tesla', 'model s', 2022)
print(e_car.get_descriptive_name())
e_car.update_odometer(100)
e_car.read_odometer()
e_car.battery.describe_battery()
e_car.fill_gas_tank()
e_car.battery.get_range()



# three ways used to modify attribute values
    # directly modifying 
my_car.odometer_reading = 1000
    
    # by using a method
my_car.update_odometer(4000)

    # incrementing values through a method
my_car.increment_odometer(200);

print(my_car.get_descriptive_name())
my_car.read_odometer()
