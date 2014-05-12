def max_in_list(newlist):
	''' (list) -> int
	Defines a a function max_in_list() that takes a list of numbers and returns
	the largest one.
	'''
	sortedlist = sorted(newlist) # sorted() sorts from min to max
	return sortedlist[-1] # returns last number i.e. max

mylist = [36, 68, 89, 8, 9, 6, 24, 23, 90, 12, 28]
print 'In a list of ' + str(mylist) + ', the max is:'
print max_in_list(mylist)