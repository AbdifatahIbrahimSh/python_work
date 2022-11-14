# name =  input("What is your name?: ")
# age =  input("How old are you?: ")
# print(f"My name is {name.title()}. I am {age} years old")
# print(age)


# prompt
# message = "We will ask you some questions and we are expecting you to answer."
# message += "\nWhat is your name? "
# name = input(message);
# print(f"Welcome {name.title()}, to our website! ")


# age = int(input("How old are you? "))

# if age >= 15:
#     print("you are old enough to vote")
#     print("have you ever voted")
# else: 
#     print("sorry, you are not allowed to vote until 15 years old")

# num = int(input("tell me a number and I will tell you if its odd or even: "))

# if num % 2 == 0:
#     print("its even")
# else: 
#     print("its odd")


# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

# while message != 'quit':
#     message = input(prompt)
    
#     if message != 'quit':
#         print(f"{message}.\n")

import re


prompt = "Tell me something and i will repeat it back to you."
prompt += "\nEnter \'quit\' to end the program: "

message = ""
# flag in python programming 
active = True

# while active: 
#     message = input(prompt)

#     if message == 'quit':
#         active = False
#     else: 
#         print(f"{message}. \n")

# while True: 
#     message = input(prompt)

#     if message == 'quit':
#         break
#     else:
#         print(f"{message}. \n")

# odd_numbers = []
# current_number = 0

# while current_number < 100:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue
#     else: 
#         odd_numbers.append(current_number)

# odd_numbers.reverse()
# print(odd_numbers)



# unconfirmed_users = ['hodo', 'sumaya', 'idil', 'huda']

# confirmed_users = []

# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#     print(f"Verifying user: {current_user.title()}")
#     confirmed_users.append(current_user)

# print(f"\nThe following users have been confirmed: ")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())



# animals = ['dog', 'cat', 'snake', 'lion', 'cat', 'tiger', 'mouse', 'cat']

# print(animals)
# print('\n')
# while 'cat' in animals: 
#     animals.remove('cat')

# print(animals)

responses = {}

polling_active = True
while polling_active: 
    name = input("What is your name? ")
    response = input("What is the name of the first school you attended? ")
    repeat = input("Would you like another person to response(yes/no): ")

    responses[name] = response

    if repeat == 'no':
        polling_active = False

for name, response in responses.items(): 
    print(f"My name is {name.title()}.\nThe first school i attended was {response.title()}.\n")














