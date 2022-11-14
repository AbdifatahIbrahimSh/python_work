from typing import get_args


# def greet_user(username):
#     """Display greet to the user"""
#     print(f"hello, {username.title()}")


# def full_name(first, last, address='hargeisa'):
#     """Display fullname of the person"""
#     full_name = f"My fullname is {first.title()} {last.title()}. I live in {address.title()}"

#     return full_name 

# # positional arguments
# full_name('abdifatah', 'ibrahim')
# full_name('mohamed', 'mouse', 'gabiley')

# # keyword arguments
# full_name(last='faysal', first='hoodo')

# # optional arguments
# def get_formated_name(first, last, middle=''):
#     """Returns the full formated name"""
#     if middle:
#         full_name = f"{first} {middle} {last}"
#     else: 
#         full_name = f"{first} {last}"
    
#     return full_name.title()

# get_formated_name('hoodo', 'yousuf', 'faysal')


# # returning dictionary
# def build_person(first, last, age=None):
#     """Returns a dictionary of information about a person"""
#     person = {'first': first, 'last': last}
#     if age: 
#         person['age'] = age
#     return person



# musician = build_person('mohamed', 'nour', 41)


# # while True:
# #     print("\nPlease tell me your name:")
# #     print("(enter 'q' at any time to quit)")

# #     f_name = input("What is your first name: ")
# #     if f_name == 'q':
# #         break
# #     l_name = input("What is your last name: ")
# #     if l_name == 'q':
# #         break
    
# #     formated_name = get_formated_name(f_name, l_name);
# #     print(f"\nHello, {formated_name}!")

# # Passing a list 

# def greet_users(names):
#     """Prints a simple greeting to each user in the list"""
#     for name in names: 
#         print(f"Hello, {name.title()}")


# users = ['mohamed', 'jama', 'hoodo', 'salma']   


# def print_models(un_printed_designs, completed_models):
#     """Prints the designs"""
#     while un_printed_designs:
#         current_design = un_printed_designs.pop();
#         print(f"Printing {current_design}")
#         completed_models.append(current_design)


# def show_compeleted_models(completed_models):
#     """Show the printed models"""
#     print("\nThe following are the printed models:")
#     for completed_model in completed_models:
#         print(f"{completed_model.title()}")



# un_printed_designs = ['gaxnoug', 'hoodale', 'gacaweyne']
# completed_models = []

# print_models(un_printed_designs[:], completed_models);

# show_compeleted_models(completed_models)

# print(un_printed_designs)
# print(completed_models)


# Passing Arbitrary number of arguments

# def find_sum(*numbers):
#     """Returns the sum of arbitrary number of values"""
#     sum = 0
#     for number in numbers:
#         sum += number

#     return sum

# print(find_sum(1, 2, 3, 4, 5))


# def make_pizza(size, *toppings):
#     """Make pizza"""
#     print(f"\nMaking {size}-inch pizza for the following toppings:")
#     for topping in toppings:
#         print(f" - {topping.title()}")
   

# make_pizza(4, 'hamse')
# make_pizza(9, 'mohamed', 'jama', 'nour')


# def buil_profile(first_name, last_name, **user_info):
#     """Build a dictionary to store anything we know about the user"""
#     user_info['first'] = first_name
#     user_info['last'] = last_name
#     return user_info;


# user_profile = buil_profile('hoodo', 'faysal')

# print(user_profile)

# Storing functions into a modules





