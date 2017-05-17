list1 = list(range(1, 1000, 3))
list2 = list(range(1, 1000, 5))
list3 = set(list1) | set(list2)
print sum(list3)
