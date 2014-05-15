def char_freq(text):
	''' (str) -> dictionary
	Defines a function char_freq() that takes a string and builds a frequency listing 
	of the characters in a dictionary.
	'''
	freq_list = {key: 0 for key in text}
	for letter in text:
		freq_list[letter] += 1
	return freq_list

something = "abbabcbdbabdbdbabababcbcbab"
print something
print char_freq(something)