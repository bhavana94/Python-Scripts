"""
Largest prime factor of the number 600851475143
"""

def factorsofno(n):
    factors = []
    for i in range(1, n+1):
        if n % i ==0:
		factors.append(i)
    return factors

def isPrime(number):
	return len(factorsofno(number)) == 2

allfac = factorsofno(600851475143)
largetnumber = 0

for k in allfac:
	if isPrime(k) and k > largetnumber:
		largetnumber = k

print largetnumber


