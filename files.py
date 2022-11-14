"""We will learn how to read files and write in to"""

# printing the entire content

# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
#     print(contents)


# printing the contents line by line

# filename = "pi_digits.txt"
# with open(filename) as file_object: 
#     for line in file_object:
#         print(line.rstrip())


# making a list of lines from a file
# filename = 'pi_digits.txt'
# with open(filename) as file_object:
#     lines = file_object.readlines()

# for line in lines:
#     print(line.rstrip())


# working file's contents


# filename = 'pi_digits.txt'
# with open(filename) as file_object: 
#     lines = file_object.readlines()

# pi_string = ''
# for line in lines:
#     pi_string += line.strip()
    


# finding if my birthday inside the first 30 decimal places of pi
# print(pi_string)
# birthday = input("What is your birthday? (enter in mmddyy format)!: ")

# found = True
# while found:
#     if birthday in pi_string: 
#         print("Yeah, you are in")
#         found = False
#     else: 
#          birthday = input("What is your birthday? (enter in mmddyy format)!: ")



# reading names.txt file and replacing each nimco and nawal to degan and maftuxa
# filename = 'names.txt'
# with open(filename) as file_object: 
#     lines = file_object.readlines()

# names = ''
# for line in lines:
#     names += f"{line.strip()} "

# print(names)
# replaced_names = names.replace('Nawal', 'Degan')
# replaced_names_two = replaced_names.replace('Nimco', 'Maftuxa')
# print(replaced_names_two)

# writting lists.txt file 
# filename = 'lists.txt'
# with open(filename, 'w') as f:
#     f.write("the new text will erase the existing text \n")
#     f.write("this will also go next the first line\n")

# filename = 'lists.txt'
# with open(filename, 'a') as f:
#     f.write("The next line will come the after the first one\n")
    

# Reading and replacing files 
# filename = 'names.txt'
# with open(filename, 'r+') as f:
#     lines = f.readline();
    
# names = ''
# for line in lines:
#     names += line;

# replaced_names = names.replace('Nawal', 'Degan')

# with open(filename, 'w') as f:
#     f.write(replaced_names)



# You can also read and write files like this by explicitly closeing the file 
# filename = 'names.txt'

# file_object = open(filename)
# contents = file_object.read()
# file_object.close()
# print(contents)
# names = ['khadra', 'hoodo', 'samia', 'shayma', 'najma', 'nacima', 'nasim']

# filename = 'yow.txt'
# with open(filename, 'w') as f:
#     f.writelines(names)

# filename = 'text_files/names.txt'

# with open(filename) as f:
#     lines = f.readlines()
    

# for line in lines:
#     print(line.strip())



























