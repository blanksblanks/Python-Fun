def length(given):
	''' (list or str) -> int
	Defines a function that computes the length of a given list or string. 
	Assuming built-in len() function doesn't exist.
	'''
	counter = 0
	for item in given:
		counter += 1
	return counter

something = input("Enter string or list : ")
print ("Length is " + str(length(somelist)))
