# #creating list
# names = ['Mohamed', 'Hussien', 'Ali', 'Nour'];

# # accessing list elements 
# names[0];

# # modifying elements 
# names[0] = 'Abdifatah';
# names[-1] = 'Hoodo';

# # adding elements in a list
#     # append, insert
# names.append('Mohamed');
# names.append("Mohamed");
# names.append("Nour");
# names.append("Hoodo");
# names.insert(3, 'Najma');

# # removing elements in the list 
#     # del statement, pop, remove 
# del names[0];
# names.pop();
# removed = names.pop(2);
# names.remove('Ali');

# # sorting a list 
#     # temporary sort sorted function, and permananet sort
# names.sort();


# names.reverse();

# names_length = len(names);

# cities = ['Hargiesa', 'Burco', 'Borama', 'Burco'];


# for city in cities:
#     print(city);
#     cities.remove(city);

# # print(cities);

# # numeric lists 
# for n in range(1, 6): 
#     print(n);

# numbers = list(range(2,11, 2));
# print(numbers);

# print(f"Maximum number is : {min(numbers)}");

# for value in range(1, 11):
#     #print(value ** 2);

# list comprehension 
    # 


# sum = [expression (condition is optional), iterable(for in) condition is optional ];
# from copy import copy

# slicing 
from cmath import rect
from re import L
from traceback import print_tb


names = ["Hussein", "jama", "Huda", "Amoun", "Hoodo"];

# sliced_names = names[0:3];
# sliced_names1 = names[:2];
# sliced_names2 =  names[2:];

# #negative slice 
# sliced_names3 = names[-3:];

# print(names);
# print(sliced_names);
# print(sliced_names1);
# print(sliced_names2);
# print(sliced_names3);


# for name in names[:3]:
#     print(name.title().lower());

#copying a list 
# hoppies = ['Playing', 'Reading', 'Going out', 'Listening'];

# my_friend_hoppies = hoppies[:]; # deep copy
# my_second_friend_hoppies = hoppies; # shallow copy


# hoppies.append('Laughing');
# my_second_friend_hoppies.pop(3);

# print(f"My Hoppies: ")
# print(hoppies);

# print(f"\nMy Friend's hoppies: ");
# print(my_friend_hoppies);

# print(f"\nMy Second Friend hoppies");
# print(my_second_friend_hoppies);


# tuple: collection of items that doesn't change

# dimension = (10, 45);
# print(dimension[0]);
# print(dimension[1]);

# dimensions= (1, 2, 4, 5);
# print("Original Dimension");
# for dimension in dimensions:
#     print(dimension);

# print("Redefined Dimenstion");
# dimensions = (6, 7, 8, 9, 10);
# for dimension in dimensions:
#     print(dimension);


# name = 'Mohamed';
# # if (name == 'Mohamed'):
# #     print('Yeah, they\'re equal');


# username = 'admin';
# password = '123';

# # and evaluated to true if both of the condition are true
# # if ((username == 'admin') and (password == '123')):
# #     # s


# super_users = ['Mohamed', 'Jama', 'Hinda'];


# user = 'Ali';
# if (user in super_users):
#     print(f"Welcome, {user.title()}");
# else: 
#     print('You are not part of the super_users list');


# age = 7
# if (age < 0):
#     price = 0;
# elif (age <= 10):
#     price = 10;
# elif (age <= 20):
#     price = 20;

# print(f"My aage {price} ");

# names = [];
# if not names: 
#     names.append('Mohamed');

# print(names);




































