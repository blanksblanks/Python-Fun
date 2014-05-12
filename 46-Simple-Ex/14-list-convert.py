def list_convert(wordlist, intlist = []):
	''' (list) ->
	Defines a function that maps a list of words into a list of integers representing
	the lengths of the correponding words.
	'''
	for i in range(len(wordlist)):
		intlist.append(len(wordlist[i]))
	return intlist

ourzoo = ['cat','snake','lizard','fish','frog', 'dragon', 'gecko']

print 'List of words : ' + str(ourzoo)
print 'Converted list containing word lengths : '  + str(list_convert(ourzoo))