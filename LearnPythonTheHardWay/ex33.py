def append_number(number, acount, scan):
	i = 0
	while i < acount:
		print "At the top i is %d" % i
		number.append(i)
		i += scan
		print "Numbes now: ", number
		print "At the bottom i is %d" % i
	return number

numbers = []
numbers = append_number(numbers, 8, 2)

print "The numbers: ", numbers

print numbers