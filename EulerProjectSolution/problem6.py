"""
Difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
def diff_sum():
    a = []
    p=1
    sum = 0    
    sum2 = 0
    diff = 0
    for i in range(1,101):
        p = i**2
        sum = sum + p
    for k in range(1,101):
        sum2 = sum2 + k
        res = sum2 **2
    diff = res - sum
    return diff

print diff_sum()



