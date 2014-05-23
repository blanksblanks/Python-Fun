def reverse(text):
    return text[::-1]

def is_palindrome(text):
	''' (str) -> bool -> str
	Defines a function is_palindrome() that recognizes palindromes
	(i.e. words that look the same written backwards)
	'''
	text = text.lower()
	punctuation = ['"', "'", '.', ',', ' ', '?', '!', ':', ';', '-', ')',
				   '(', ']', '[', '\\', '/']
	for x in punctuation: # for loop checks text for x items from tuple
		text = text.replace(x, '') # removes x items
	if text == reverse(text):
		return True
	else:
		return False

if __name__ == "__main__":
	'''
	If this file is being imported from another module, __name__ will be
	set to the module's name." By doing the main check, you can have that
	code only execute when you want to run the module as a program and not
	have it execute when you just want to import your module and call your
	functions themselves.
	'''
	something = raw_input("Enter text: ")
	if is_palindrome(something) == True:
		print "Yes, it is a palindrome"
	else:
		print "No, it is not a palindrome"

