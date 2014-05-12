# encoding=utf-8

def translate(text, consonants = 'bcdfghjklmnpqrstvwxyz'):
	''' (text) -> text
	Defines function translate() that will translate a text into "rövarspråket"
	(Swedish for "robber's language"), i.e. double every consonant and place
	an occurrence of "o" in between.
	'''
	for x in consonants:
		text = text.replace(x, x + 'o' + x)
	return text

print u"This will translate text into 'rövarspråket.'"
print "'This is fun' becomes :" + translate('This is fun')
print ""

something = str(raw_input('Enter some text : '))
print 'Translation : ' + str(translate(something))
