def lengths_for(wordlist):
	''' (strlist) -> intlist
	Defines a program that maps a list of words into integers representing
	the lengths of the correponding words. Method 1: using a for-loop
	'''
	intlist = []
	for i in range(len(wordlist)): # for word in words:
		intlist.append(len(wordlist[i])) # .append(len(word))
	return intlist

def lengths_map(words):
	''' (strlist) -> intlist
	Method 2: using the higher order function map()

    map(function, sequence[, sequence, ...]) -> list
    Return a list of the results of applying the function to the items of
    the argument sequence(s).  If more than one sequence is given, the
    function is called with an argument list consisting of the corresponding
    item of each sequence, substituting None for missing values when not all
    sequences have the same length.  If the function is None, return a list of
    the items of the sequence (or a list of tuples if more than one sequence).
	'''
	return map(len, words)

def lengths_list(words):
	''' (strlist) -> intlist
	Method 3: using list comprehensions
	'''
	return [len(word) for word in words]

ourzoo = ['cat','snake','lizard','fish','frog', 'dragon', 'gecko']
print 'Using for-loop : ' + str(lengths_for(ourzoo))
print 'Using higher order map function : ' + str(lengths_map(ourzoo))
print 'Using list comprehensions : ' + str(lengths_list(ourzoo))