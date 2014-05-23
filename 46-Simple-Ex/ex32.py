from ex8 import is_palindrome


def palidrome_io(filepath):
	""" (file) -> str -> bool -> str
	Another version of a palindrome recogniser that accepts a file name from
	the user, reads each line, and prints the line to the screen if it is a
	palindrome.
	"""
	file = open(filepath)
	for line in file.read().split("\n"):
		if is_palindrome(line):
			print line

if __name__ == "__main__":
    palidrome_io('ex32.txt')