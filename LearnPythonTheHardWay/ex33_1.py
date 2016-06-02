def append_number(numbers, acount, scan):
	for i in range(0, acount, scan):
		print "At the top number is %d" % i
		numbers.append(i)
		i += scan
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i 
	return numbers

numbers = []
numbers = append_number(numbers, 8, 1)

print "The numbers: ", numbers

print numbers