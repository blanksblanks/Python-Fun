def is_vowel(letter):
	''' (str) -> boolean
	Defines a function that takes a character (i.e. a string of length 1)
	and returns True if it is a vowel, False if otherwise
	'''
	letter = letter.lower() # to allow for capitalization
	return letter == ('a' or 'e' or 'i' or 'o' or 'u')

# HOW TO DEFINE EXCEPTION CLASS: class ErrorName(Exception):
# def __init__(self, vars): Exception.__init__(self) self.var = var
class CharacterInputException(Exception):
	'''A user-defined exception class.'''
	def __init__(self, length, reqlength):
		Exception.__init__(self)
		self.length = length
		self.reqlength = reqlength

# HOW TO RAISE ERROR: try: raise...except ErrorName as err:... else:
try:
	text = str(raw_input('Enter a character : '))
	if len(text) != 1: # raises error if string isn't length
		raise CharacterInputException(len(text), 1)
except CharacterInputException as err:
		print ('CharacterInputException: The input was ' + \
			  '{} long, expected only {} character') \
			  .format(err.length, err.reqlength)
else:
	if is_vowel(text): # if returns true
		print 'Yes, it is a vowel'
	else:
		print 'No, it is not a vowel'