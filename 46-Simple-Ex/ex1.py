# HOW TO MAKE FUNCTION: def name(variables): statements

def max(a, b):
	''' (int, int) -> int
	Defines a function max_fxn() that takes two numbers as arguments
	and returns the largest of them. Python has max() built-in already,
	but this is good exercise.
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
print 'The largest number is ' + str(max(one, two)) + '.'