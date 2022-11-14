"""Develops a program that guest groups each five students randomly
   Developer: Abdifatah
   Date: 31 October, 2022
   Time: 1:30pm
"""

from random import randint, choice

filename = 'text_files/names.txt'
with open(filename) as f:
    contents = f.read()


names = contents.split('\n')

choosed_five = []
while len(choosed_five) < 5:
    name = choice(names)
    if name not in choosed_five and name:
        choosed_five.append(name)
        names.remove(name)

print(choosed_five)
print(len(names))

if len(names) > 0:
    with open(filename, 'w') as f:
        for name in names:
            f.write(f"{name}\n")

    