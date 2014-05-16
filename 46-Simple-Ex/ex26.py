def max_in_list(numbers):
	'''
	Using the higher order function reduce(), write a function max_in_list()
	that takes a list of numbers and returns the largest one. Then ask
	yourself: why define and call a new function, when I can just as well call
	the reduce() function directly?
	
	reduce(...)
    reduce(function, sequence[, initial]) -> value
    Apply a function of two arguments cumulatively to the items of a sequence,
    from left to right, so as to reduce the sequence to a single value.
    For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
    ((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
    of the sequence in the calculation, and serves as a default when the
    sequence is empty.
	'''
	return reduce(max, numbers)

print max_in_list([89, 9, 8, 98, 88, 189, 99])