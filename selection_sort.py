
import math

list = [5, 2, 1, 3, 4, 12]
print(list)
for i in range(0, len(list) - 2):
    m = i
    for j in range(i + 1, len(list) - 1):
        if list[j] < list[m]:
            m = j
            temp = list[i]
            list[i] = list[m]
            list[m] = temp
        
print(list)
    