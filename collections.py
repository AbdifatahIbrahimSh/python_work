
"""
    Collection properties in python
        - ordered
        - mutable
        - indexed
        - allow duplates

    Collections in Python:
        1. List (ordered, mutable, indexed, allow duplicates)
        2. Tuple (ordered, indexed, allow dupliactes)
        3. Set (mutable)
        4. Dictionary (mutable, ordered,)
"""

# list
# names = {'name', 'huda', 'ibrahim', 'mouse', 'mouse'}
# ages = {20, 34, 20}
# names.update(ages)
# names.add('abdifatah')

# names.remove('huda')
# names.discard('name1')
# print(names)


set1 = {1, 2, 3, 4, 5}
set2 = {2, 4, 5, 6, 7, 8}
union = set1.union(set2)
intersection = set1.intersection(set2)

set1.symmetric_difference_update(set2)



print(set1)
print(set2)
print(union)
print(intersection)















