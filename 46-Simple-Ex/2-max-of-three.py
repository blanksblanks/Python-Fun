def max_of_three(a, b, c):
	if (a > b) & (a > c):
		return a
	elif b > c:
		return b
	else:
		return c

print max_of_three(2, 4, 6)
print max_of_three(6, 2, 4)
print max_of_three(4, 6, 2)