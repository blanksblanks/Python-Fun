# Defines a function reverse() that computes the reversal of a string

def reverse(text):
	return text[::-1]

something = str(raw_input("Enter a string : "))
print "Reversal : " + reverse(something)

