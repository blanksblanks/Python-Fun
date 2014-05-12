def generate_n_chars(n, c):
	''' (int, str) -> str
	Defines a function generate_n_chars() that takes an integer n and a character c and 
	returns a string, n characters long, consisting only of c's. For example, 
	generate_n_chars(5,"x") should return the string "xxxxx". (Python is unusual in that 
	5 * "x" that will evaluate to "xxxxx", but ignore that for now.)
	'''
	counter = 1
	nchars = c # starts with one character
	running = True

	while running:
		nchars += c
		counter += 1
		if counter == n:
			running = False
			return nchars 

print generate_n_chars(5, "x")

class TypeException(Exception):
	'''A user-defined exception class.'''
	def __init__(self, typeof, reqtype):
		Exception.__init__(self)
		self.typeof = typeof
		self.reqtype = reqtype

class CharacterInputException(Exception):
	'''A user-defined exception class.'''
	def __init__(self, length, reqlength):
		Exception.__init__(self)
		self.length = length
		self.reqlength = reqlength

try:
	number = int(raw_input('Enter a number : '))
except ValueError:
	print ('ValueError: The input should be of int type.')
	number = int(raw_input('Enter a number : '))
try:
	text = str(raw_input('Enter a character : '))
	if len(text) != 1: # raises error if string isn't length
		raise CharacterInputException(len(text), 1)
except CharacterInputException as err:
		print ('CharacterInputException: The input was ' + \
			  '{} long, expected only {} character') \
			  .format(err.length, err.reqlength)
else:
	print generate_n_chars(number, text)