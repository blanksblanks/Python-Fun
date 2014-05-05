# Defines a function max() that takes two numbers as arguments
# and returns the largest of them

# HOW TO MAKE FUNCTION: def name(variables): statements

def max_fxn(a,b): # because Python has max() built-in already
	if a > b: 
		return a
	elif a==b:
		return "They're the same."
	else:
		return b

print max_fxn(10,20)
print max_fxn(10,10)
print max_fxn(12, 5)