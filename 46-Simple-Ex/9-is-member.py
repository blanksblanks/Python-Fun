def is_member(value, alist):
	''' (value, list) -> bool
	Defines a function is_member() that takes a value (i.e. a number, string, etc.)
 	x and a list of values a, and returns True if x is a member of a,
	False otherwise. (Assuming there is no built-in in operator.)
	'''
	for item in alist:
		if item == value:
 			return True
 	else: return False # remember: indentation important here

our_zoo = ['cat','snake','lizard','fish','frog', 'dragon', 'gecko']
animal = raw_input("Enter an animal to check if we have it in our zoo : ")
 
if is_member(animal, our_zoo):
	print ("The animal is present in our zoo")
else:
	print ("The item is not present in our zoo")

print("The list of animals in our zoo is: " + str(our_zoo))
