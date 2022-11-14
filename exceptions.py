"""Write code to handle exceptions"""

# by using try-execpt we can handle exceptions
# try:
#     print(5 / 0)
# except ZeroDivisionError:
#     print("we can't divide by zero (0)")

# print("we will print anything beyond that")

# # dividing any two numbers entered with handling zerodivisionerror 
# print("Write two numbers to get thier division")
# print("Write 'q' to quit")
# while True:
#     first = input("Enter first number: ")
#     if first == 'q': 
#         break
#     second = input("Enter second number: ")
#     if second == 'q':
#         break

#     try: 
#         if first and second:
#             total = int(first) / int(second)
#         else: 
#             print("Enter a valid number")
#     except ZeroDivisionError:
#         print("we can't divide by zero\n")
#     else:
#         print(f"{total}\n")


# # handling not found files to read 
# filename = 'found.txt'
# try:
#     with open(filename, encoding='utf-8') as f:
#         contents = f.read()
# except FileNotFoundError:
#     print(f"{filename} not found")
# else: 
#     print(contents)


# # failing silently by passing 'pass' and return in except
# filename = 'mow.txt'
# try: 
#     with open(filename) as f:
#         f.read()
# except FileNotFoundError:
#     pass
    