def max_in_list(numbers):
	''' (list) -> int
	Defines a function max_in_list() using the higher order function reduce().
	Why define and call a new function, when one can call reduce() directly?
	
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