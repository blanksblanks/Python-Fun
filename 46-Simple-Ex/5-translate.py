# encoding=utf-8

# Defines function translate() that will translate a text into "rövarspråket"
# (Swedish for "robber's language"), i.e. double every consonant and place
# an occurrence of "o" in between.

def translate(text, consonants = 'bcdfghjklmnpqrstvwxyz'):
	for x in consonants:
		text = text.replace(x, x + 'o' + x)
	return text

print u"""This will translate a text into 'rövarspråket' (Swedish
for robber's  language) and double every consonant with
'o' in between. For example, 'This is fun' becomes : """
print translate('This is fun')
print ""

something = str(raw_input('Enter some text : '))
print 'Translation : ' + str(translate(something))
