def filter_long_words(alist, n):
	''' (list, int) -> list
	Defines  a function filter_long_words() that takes a list of words and an
	integer n and returns the list of words that are longer than n.
	'''
	newlist = []
	for i in range(len(alist)):
		if len(alist[i]) > n:
			newlist.append(alist[i])
	return newlist

ourzoo = ['cat','snake','lizard','fish','frog', 'dragon', 'gecko']
minlength = 5

print 'List of words : ' + str(ourzoo)
print 'Filtered list containing word(s) that are longer than ' + str(minlength) + \
	  ' : '  + str(filter_long_words(ourzoo, minlength))