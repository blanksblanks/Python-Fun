def find_longest_word(words):
	''' (list) -> int
	Defines a function find_longest_word() that takes a list of words and returns the length of the longest one, using only higher order functions.
	'''
	return max(map(len, words))

print find_longest_word(['hi', 'hello', 'greetings', 'hola', 'nihao', 'howdy'])