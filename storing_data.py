"""Stores the data in a json files """

import json


# students = ['mohamed', 'jama', 'nour', 'mouse', 'hussein', 'nimco']

# # storing your data in json file using json.dump()
# filename = 'students.json'
# with open(filename, 'w') as f:
#     json.dump(students, f)

# # loading data from json file using json.load()
# with open(filename) as f:
#     loaded_contents = json.load(f)

# # saving user generated information into json files 
# filename = 'username.json'
# with open(filename, 'w') as f:
#     username = input("What is your name? ")
#     json.dump(username, f)
#     print(f"{username}, We will remember your when you when you come back")

# # readig user generated data from a json file 
# with open(filename) as f:
#     username = json.load(f)
#     print(f"Welcome back {username}")


# # Storing data in a json file
# filename = 'name_of_user.json'
# try: 
#     with open(filename) as f:
#         username = json.load(f)
# except FileNotFoundError:
#     username = input("What is your name? ")
#     with open(filename, 'w') as f:
#         json.dump(username, f)
#         print(f"Welcome {username}")
# else:
#     print(f"Welcome back {username}!")




def get_stored_username():
    """Gets the stored username in the json file"""
    filename = 'names_of_boys.json'
    try:
        with open(filename) as f:
            username = json.load(f);
    except FileNotFoundError:
        return None
    else:
        return username

def  get_new_username():
    """Takes a new username and saves into the file"""
    filename = 'names_of_boys.json'
    username = input("Tell me your username: ")
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username.title()}")
    else: 
        username = get_new_username()
        print(f"Hello, {username.title()} We'll remember you the next time you visit us.")


greet_user()

