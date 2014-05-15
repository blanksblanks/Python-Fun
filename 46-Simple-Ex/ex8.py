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
		return "Yes, it is a palindrome" # if true
	else:
		return "No, it is not a palindrome"

something = raw_input("Enter text: ")
print is_palindrome(something)

