# encoding=utf-8

def swedish_translate(text):
	''' (str) -> str
	Defines a function swedish_translate() that takes a list of English words and
	returns a Swedish words. The dictionary and its key:value pairs represent a small
	bilingual lexicon of English and Swedish words used in a holiday card.
	'''
	dictionary = {"merry":"god",
                  "christmas":"jul",
                  "and":"och",
                  "happy":"gott",
                  "new":"nytt",
                  "year":"år"}
	text = text.lower()
	for word in text.split(" "):
		if (str(dictionary.get(word))) != False:
			text = text.replace(word, str(dictionary[word]))
			#unlike dic[word], dic.get(word) DOESN'T cause error if key not found
		else:
			text = "This could not be translated."
	return text

something = "Merry Christmas and Happy New Year"
print "English : " + something
print "Swedish : " + swedish_translate(something)