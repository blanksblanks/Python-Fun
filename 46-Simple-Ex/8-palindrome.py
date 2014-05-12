def reverse(text):
    return text[::-1]

def is_palindrome(text):
	''' (str) -> bool
	Defines a function is_palindrome() that recognizes palindromes
	(i.e. words that look the same written backwards)
	'''
	text = text.lower()
	punctuation = ['"', "'", '.', ',', '?', '!', ':', ';', '-', ')', '(', ']', '[', '\\', '/']
	for x in punctuation: # for loop checks text for x items from tuple
		text = text.replace(x, '') # removes x items
	return text == reverse(text) 

something = raw_input("Enter text: ")
if is_palindrome(something): # if true
    print "Yes, it is a palindrome"
else:
    print "No, it is not a palindrome"
