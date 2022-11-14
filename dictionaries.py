# Dictionaries in Python
from webbrowser import get


student = {
    'first': 'mohamed',
    'last': 'mouse',
    'age': 30,
    'address': 'hero-awr'
}

# # accessing values 
# print(student['first'])
# print(student['last'])
# print(student['address'])

# # adding new key-value pairs
# student['phone'] = 4507262;
# student['class'] = '4c'

# print(student);

# # modifying values 
# student['address']  = 'masalaha'

# print(student);

# # removing key-value pairs
# del student['age']

# print(student)

# get method 
# gender = student.get('gender',  'we don\'t have gender key')

# print(gender)


# looping throught the dictionaries 
    # all key-value pairs

favorite_languages = {
    'mohamed': ['c', 'java'],
    'hamse': ['javascript', 'python'], 
    'hoodo': ['rupy', 'c', 'php'],
    'najma': ['javascript'],
    'ahmed': ['html', 'css', 'javascript'],
    'muna': ['java']
}

# print(f"student dictionary: ")
# for key, value in student.items():
#     print(f"\t{key}: {value} ")   

# for name, language in favorite_languages.items(): 
#     print(f'{name}\'s favorite language is {language.title()}');





# looping through all keys 
# for name in favorite_languages.keys():
#     print(name.title())


# default python looping throught the dictionaries returns the keys 
# names = [];
# for name in favorite_languages:
#     names.append(name)
# print(names)


# friends = ['mohamed', 'najma'];

# for name in sorted(favorite_languages):
#     print(f"Hi,  {name.title()}")
#     if name in friends:
#         language = favorite_languages[name].title()
#         print(f"\t{name.title()}, I see you love {language}")


# looping through all values 
# for language in sorted(set(favorite_languages.values())):
#     print(language.title())


# nesting 
    # dictionaries in a list 

# student_0 = {'first': 'abdifatah', 'phone': 4507262, 'age': 22}
# student_1 = {'first': 'hoodo', 'phone': 3914163, 'age': 20}
# student_2 = {'first': 'shayma', 'phone': 6667896, 'age': 18}


# students = [student_0, student_1, student_2]
# # for student in students:
#     # print(student)

# teachers = []
# for number in range(10):
#     new_teacher = {'first': 'mouse', 'age': 20, 'salary': 400}
#     teachers.append(new_teacher)

# for teacher in teachers[:5]:
#     print(teacher)
# print("...")
# print(f"\ntotal number of teachers is: {len(teachers)}")


    # lists in dictionary
# for name, languages in favorite_languages.items():
#     if len(languages) > 1:
#         print(f"{name.title()}\'s favorite languages are: ")
#         for language in languages:
#             language = language.title()
#             print(f"\t {language}")
#         print('')
#     else: 
#         print(f"{name.title()}\'s favorite language is: {languages[0].title()}")
#         print('')
        

    # dictionary in a dictionary

users = {
    'abdiyare': {
        'first': 'abdifatah', 
        'last': 'ibrahim',
        'phone': 4507262
    }, 
    'hodaley': {
        'first': 'hoodo', 
        'last': 'faysal',
        'phone': 7313018
    }
}

for username, user_info in users.items():
    print(f"Username: {username.title()}") 
    full_name = user_info['first'] + ' ' +  user_info['last']
    phone = user_info['phone']

    print(f"\t Full Name: {full_name.title()} \n\t Phone: {phone}")
    print('')

    















