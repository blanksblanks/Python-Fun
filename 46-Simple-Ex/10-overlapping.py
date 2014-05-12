def overlapping(list1, list2):
	''' (list, list) -> bool
	Defines a function overlapping() that takes two lists and returns
	True if they have at least one member in common, False otherwise.
	Use two nested for-loops.
	'''
	for item in list1:
		for thing in list2:
			if item == thing:
				return True
	else: return False

our_zoo = ['cat','snake','lizard','fish','frog', 'dragon', 'gecko']
bronx_zoo = ['lion', 'tiger', 'monkey', 'bird', 'snake']

if overlapping(our_zoo, bronx_zoo):
	print "Yes, the lists are overlapping"
else:
	print "No, the lists aren't overlapping"
