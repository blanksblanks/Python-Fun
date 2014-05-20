# encoding = utf-8

def translate(words):
	''' (strlist) -> strlist
	Defines a function translate() that uses the higher order function map() to
	take a list of English words and return a list of Swedish words
	'''
	lexicon = {"merry":"god",
	           "christmas":"jul",
	           "and":"och",
	           "happy":"gott",
			   "new":"nytt",
			   "year":"ar"}
	return map(lambda word: lexicon[word], words)

print translate(['merry', 'christmas', 'and', 'happy', 'new', 'year'])
