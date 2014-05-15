def sumList(sum_list):
	''' (list) -> int
	Defines functions sum() that sums all numbers in a list. 
	For example, sum([1, 2, 3, 4]) should return 10.
    '''
    total = 0
    for i in sum_list:
        total += int(sum_list[i-1])
    return total
 
def multiplyList(multiply_list):
	''' (list) -> int
	Defines function multiplyList() that multiplies all numbers in a list. 
	For example, multiplyList([1, 2, 3, 4]) should return 24.
    '''
    final = 1
    for i in multiply_list:
        final *= int(multiply_list[i-1])
    return final
 
myList = [1,2,3,4]
 
print ("List of numbers: " + str(myList))
print("Sum total: " + str(sumList(myList)))
print("Multiplied total: " +str(multiplyList(myList)))

# ** is supposed to refer to VarArgs parameters
# This didn't work (Examine later)

#def sumtotal(start=0, **numbers):
#	total = start
#	for number in numbers:
#		count += numbers[number]

#def multiply(initial=0, **digits):
#	final = initial
#	for digit in digits:
#		count *= digits[digit]

#print "Sum total: " + str(sumtotal([1,2,3,4]))
#print "Multiplied total: " + str(multiply([1,2,3,4]))
