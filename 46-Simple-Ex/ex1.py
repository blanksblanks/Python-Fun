# HOW TO MAKE FUNCTION: def name(variables): statements

def max_fxn(a, b): # because Python has max() built-in already
	''' (int, int) -> int
	Defines a function max_fxn() that takes two numbers as arguments
	and returns the largest of them
	'''
	if a > b: 
		return a
	elif a==b:
		return "They're the same."
	else:
		return b

# Accepts three numbers from user as arguments
one = int(raw_input('Enter first number : '))
two = int(raw_input('Enter second number: '))
print 'The largest number is ' + str(max_fxn(one, two)) + '.'