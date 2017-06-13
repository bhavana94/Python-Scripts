"""
To Find 10 001st prime number?
"""


def nthPrime(n):
    primary_list = [2]
    value = 3

    while len(primary_list) < n:
        value += 2 

        if (value % 2 == 0):
            continue

        for j in primary_list:
            if (value % j == 0):
                break
        else:
            primary_list.append(value) 			
    else:
        return max(primary_list)
        
print("output - ", nthPrime(10001))  