from ex13 import max_in_list
from ex14 import list_convert

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
