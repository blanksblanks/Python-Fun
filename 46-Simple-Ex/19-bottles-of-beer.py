def bottles_of_beer():
	''' (str, int) -> str
	Defines bottles_of_beer() function, which prints all the lyrics to "99 Bottles of Beer."
	The same verse is repeated, each time with one fewer bottle. The song is completed when
	the singer or singers reach zero.
	'''
	bob = " bottles of beer"
	for i in range(99, 0, -1):
		print str(i) + bob + " on the wall, " + str(i) + bob + "."
		print "Take one down, pass it around, " + str(i-1)  + bob + " on the wall.\n"

print bottles_of_beer()