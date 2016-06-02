# -*- coding: utf-8 -*-
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
	print "This is count %d" % number

# save as above
for fruit in fruits:
	print "A fruit of type: %s" % fruit

# we use %r cause we don't know what's in a mixed list
for i in change:
	print "I got %r" % i

elements = []

# use the range function to do 0 to 5 counts
# range函数原型： range(start, end, scan)
# start：计数从start开始，默认为0
# end: 到end结束，不包括end, 例range(0, 5) 是 [0,1,2,3,4]
# scan: 每次跳跃的间距，默认为1
for i in range(0, 6):
	print "Adding %d to the list." % i
	# append()添加到列表末位，无返回值
	elements.append(i)

for i in elements:
	print "Element was: %d" % i