def reverse(text):
	''' (str) -> str
	Defines a function reverse() that computes the reversal of a string
	'''
	return text[::-1]

# seq[a:b:c] code makes slices froms sequence a to b, using c increments
# default c is 1, giving negative step -1 returns text in reverse

something = str(raw_input("Enter a string : "))
print "Reversal : " + reverse(something)

