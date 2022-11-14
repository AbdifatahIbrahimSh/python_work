"""A class used to represent a user"""

class User:
    """Creates a user class"""

    def __init__(self, first_name, last_name):
        """Initialize an object from the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = first_name + ' ' + last_name
    
    def __str__(self):
        """Returns string repsenetation of an object"""
        return f"{self.full_name.title()}"
    def describe_user(self):
        """Describe the user by printing its full name """
        print(f"My name is {self.full_name.title()}. I am  a new user! ")

    def greet_user(self):
        """Greeting the user"""
        print(f"Hello, {self.full_name.title()}")   



user = User('mohamed', 'hassan')
user.describe_user()
print(user)


