def reverse(text):
    return text[::-1]

def palindrome_recognizer(text):
	''' (str) -> bool
	Defines a version of a palindrome recognizer that also accepts phrase
	palindromes such as, "Dammit, I'm mad!"
	Note that punctuation, capitalization, and spacing are usually ignored.
	'''
	print text
	text = text.lower()
	punctuation = ['"', "'", '.', ',', ' ', '?', '!', ':', ';', '-', ')',
				   '(', ']', '[', '\\', '/']
	for x in punctuation:
		text = text.replace(x, '')
	if text == reverse(text):
		return "Yes, it is a palindrome"
	else:
		return "No, it is not a palindrome"

a = "Go hang a salami I'm a lasagna hog."
print palindrome_recognizer(a)

b = "Was it a rat I saw?"
print palindrome_recognizer(b)

c = "Step on no pets"
print palindrome_recognizer(c)

d = "Sit on a potato pan, Otis"
print palindrome_recognizer(d)

e = "Lisa Bonet ate no basil"
print palindrome_recognizer(e)

f = "Satan, oscillate my metallic sonatas"
print palindrome_recognizer(f)

g = "I roamed under it as a tired nude Maori"
print palindrome_recognizer(g)

h = "Rise to vote sir"
print palindrome_recognizer(h)

k = "Dammit, I'm mad!"
print palindrome_recognizer(k)