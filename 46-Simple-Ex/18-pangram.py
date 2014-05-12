def pangram(text):
	''' (str) -> bool
	Defines a function to check a sentence to see if it is a pangram or not.
	A pangram is a sentence that contains all letters of the English alphabet
	at least once, for example: The quick brown fox jumps over the lazy dog.
	'''
	print text
	text = text.lower()
	alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
				'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	for letter in alphabet:
		if letter in text:
			return "Yes, it is a pangram"
	else:
		return "No, it isn't a pangram"

something = "The quick brown fox jumps over the lazy dog."
print pangram(something)

anything = raw_input("Enter a string to check if it is a pangram : ")
print pangram(anything)