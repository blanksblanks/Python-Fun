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