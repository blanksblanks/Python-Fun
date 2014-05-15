def rot13(encoded):
	''' (str) -> dic -> str
	Defines an encoder/decoder of ROT-13. ROT-13 ("rotate by 13 places") is a widely
	used example of a Caesar cipher where the shift is 13. In cryptography, a Caesar
	cipher is a very simple encryption techniques in which each letter in the plain
	text is replaced by a letter some fixed number of positions down the alphabet. The
	method is named after Julius Caesar, who used it to communicate with his generals. 
	'''
	key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u',
		   'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c',
		   'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
		   'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S',
		   'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A',
		   'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I',
		   'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}
	print encoded
	words = [words for words in encoded.split()]
	print words
	decoded = []
	for word in words:
		decoded.append("".join([key[char] if char in key.keys() else char for char in word]))
	print decoded
	return " ".join(decoded)
	print decoded

print rot13("Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!")