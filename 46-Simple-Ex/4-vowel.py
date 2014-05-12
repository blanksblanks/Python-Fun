# Defines a function that takes a character (i.e. a string of length 1)
# and returns TRue if it is a vowel, False if otherwise

# HOW TO DEFINE EXCEPTION CLASS: class ErrorName(Exception):
# def __init__(self, vars): Exception.__init__(self) self.var = var

# HOW TO RAISE ERROR: try: raise...except ErrorName as err:... else:

def is_vowel(letter):
	return letter == ('a' or 'e' or 'i' or 'o' or 'u')

class LongInputException(Exception):
	'''A user-defined exception class.'''
	def __init__(self, length, atleast):
		Exception.__init__(self)
		self.length = length
		self.reqlength = reqlength

try:
	text = str(raw_input('Enter a character : '))
	if len(text) != 1: # if string isn't length 1
		raise LongInputException(len(text), 1)
except LongInputException as err:
		print ('LongInputException: The input was ' + \
			  '{} long, expected only {} character') \
			  .format(err.length, err.reqlength)
else:
	if is_vowel(text):
		print 'True: Yes, it is a vowel'
	else:
		print 'False: No, it is not a vowel'