def list_convert(wordlist, intlist = []):
	''' (list) ->
	Defines a function that maps a list of words into a list of integers representing
	the lengths of the correponding words.
	'''
	for i in range(len(wordlist)):
		intlist.append(len(wordlist[i]))
	return intlist

def max_in_list(newlist):
	''' (list) -> int
	Defines a a function max_in_list() that takes a list of numbers and returns
	the largest one.
	'''
	sortedlist = sorted(newlist) # sorted() sorts from min to max
	return sortedlist[-1] # returns last number i.e. max

def find_longest_word(alist):
	''' (list) -> str -> int
	Defines a function find_longest_word() that takes a list of words and returns
	the length of the longest one.
	'''
	alist = list_convert(alist)
	alist = max_in_list(alist)
	return alist

ourzoo = ['cat','snake','lizard','fish','frog', 'dragon', 'gecko']

print 'List of words : ' + str(ourzoo)
print 'Longest word length : ' + str(find_longest_word(ourzoo))
