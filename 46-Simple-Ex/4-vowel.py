class LongInputException(Exception):
	'''A user-defined exception class.'''
	def __init__(self, length, atleast):
		Exception.__init__(self)
		self.length = length
		self.reqlength = reqlength

def is_vowel(letter):
	return letter == ('a' or 'e' or 'i' or 'o' or 'u')

try:
	text = str(raw_input('Enter a character : '))
	if len(text) != 1:
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