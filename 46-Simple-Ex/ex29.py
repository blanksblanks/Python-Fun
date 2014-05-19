def filter_long_words(words, n):
	''' (list, int) -> list
	Using higher order function filter(), defines a function filter_long_words()
	that takes a list of words and an integer n and returns the list of words
	that are longer than n.
	'''
	return filter(lambda x: len(x) > n, words)

lista = ['super', 'duper', 'trooper', 'supercalifragilisticexpialidocious', \
		 'bomb', 'supertastic', 'great', 'good', 'aight', 'alright'] 
limit = 5
print 'Printing list of words longer than ' + str(limit) + '...'
print filter_long_words(lista, limit)