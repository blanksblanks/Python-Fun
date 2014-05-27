def is_semordnilap(filepath):
	''' (file) -> str -> list
	According to Wikipedia, a semordnilap is a word or phrase that spells a
	different word or phrase backwards. ("Semordnilap" is itself "palindromes"
	spelled backwards.) This is a semordnilap recogniser that accepts a file name 
	(pointing to a list of words) from the user and finds and prints all pairs
	of words that are semordnilaps to the screen. For example, if "stressed"
	and "desserts" is part of the word list, the the output should include the
	pair "stressed desserts". Each pair by itself forms a palindrome!
	'''
	file = open(filepath)
	words = file.read().split() # splits into each word
	semordnilaps = [] # init list
	for first in words:
		for second in words:
			if len(first) > 1: # to ensure 'I' and 'a' are not counted
				if first == second[::-1]: # compares first to list of second words
					semordnilaps.append(first + ' ' + second)
	return semordnilaps

if __name__ == "__main__":
	print is_semordnilap('ex32.txt')