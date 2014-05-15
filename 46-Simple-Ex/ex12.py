def histogram(alist):
	''' (list[int]) -> str
	Defines histogram() function that takes a list of integers and prints a histogram.
	For example, histogram([4, 9, 7]) should print: **** ********* *******
	'''
	for i in range(len(alist)): # e.g. range(4) returns [0, 1, 2, 3]
		print (alist[i] * '*') 

inputlist = [4, 9, 7]
histogram(inputlist)