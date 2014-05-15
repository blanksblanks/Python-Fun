import re # imports regular expression module

def correct(text):
	'''
	Defines a simple "spelling correct" function correct() that takes a string and sees
	to it that 1) two or more occurrences of the space character is compressed into one,
	and 2) inserts an extra space after a period if it is directly followed by a letter.
	Uses regular expression: re.sub(pattern, repl, string, count=0, flags=0)
	'''
	text = re.sub(r'( )+', r'\1', text) # reduces 2+ spaces to 1
	text = re.sub(r'[.]([a-zA-Z])', r'. \1', text) # inserts space after '.Aa-Zz'
	return text

print correct("This   is  very funny  and    cool.Indeed!")