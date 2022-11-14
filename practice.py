import os 
from gpa_program import GPA
# Removes any element contain 'a' character from the list
names = ['nawal', 'nawal', 'huda', 'amoun', 'nimco', 'huda', 'idil', 'sumaya',  'asma','idiris', 'suber', 'gulied']

# print(names)

# index = 0;
# while index < len(names):
#     if 'a' in names[index]:
#         names.pop(index)
#         index -= 1
#     index += 1
# print(names)

# string = f"|{'CourseName':^40s}| {'Mohamed'}"
# print(string)   

# filename = "C:/users/'Abdifatah Ibrahim'/Desktop/python_work/text_files/separator.txt"
# with open(filename, 'w') as f:
#     f.write("new path")

# list comprehensions
# filtered = [name for name in names if 'a' not in name]
# print(filtered)



transcript = {
    'Introduction to Database': 100,
    'Discrete Mathematics': 100,
    'Data Science': 90,
    'Advanced Programming': 94,
    'English Junior III ': 91,
}


my_gpa = GPA(transcript);
print(my_gpa.print_gpa())



