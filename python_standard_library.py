from random import randint
from random import choice

random_list = []

for number in range(10):
        random_list.append(randint(1, 100))

print(random_list)

choiced = choice(random_list)

print(choiced)