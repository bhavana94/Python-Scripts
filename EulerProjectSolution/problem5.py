"""
Smallest positive number that is evenly divisible by all of the numbers from 1 to 20
"""
primes = [2,3,5,7,11,13,17,19]
prod = 1 
for p in primes:
    n = 2
    prod *= p
    while (p**n < 21):
        prod *= p
        n += 1

