"""
Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

def fibobacci(n):
	if n<=1:
		return n
	else:
		return (fibobacci(n-1)+fibobacci(n-2))
b = []
for i in range(0,4000000):
	b.append(fibobacci(i))

print sum(k for k in b if not k%2)

	
