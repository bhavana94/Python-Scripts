"""
Largest palindrome from product of two 3 digit number
"""

largest_palin = 0

for i in range(999, 100, -1):
	for j in range(i, 100, -1):
		x = i * j
		if x > largest_palin:
			s = str(i * j)
			if s == s[::-1]:
				largest_palin = i * j

print largest_palin

