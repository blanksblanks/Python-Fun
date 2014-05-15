def max_of_three(a, b, c):
	''' (int, int, int) -> int
	Defines a function max_of_three() that takes three numbers as 
	arguments and returns the largest of them.
	'''
	if (a > b) & (a > c):
		return a
	elif b > c:
		return b
	else:
		return c

one = int(raw_input('Enter the first number : '))
two = int(raw_input('Enter the second number : '))
three = int(raw_input('Enter the third number : '))
print 'The largest number is ' + \
	  str(max_of_three(one, two, three)) + '.'
