"""
Find the sum of all the multiples of 3 or 5 below 1000
"""

list1 = list(range(1, 1000, 3))
list2 = list(range(1, 1000, 5))
list3 = set(list1) | set(list2)
print sum(list3)
