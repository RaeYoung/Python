ten_things = "Apples Oranges Crows Telophone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
	# 数组保存在栈里，从下往上保存，pop时先弹出最后保存的
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	stuff.append(next_one)
	print "There's %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
# 坐标-1为列表中倒数第一个元素
print stuff[-1]
# pop后会返回pop出的元素
print stuff.pop()
# 用空格连接stuff
print ' '.join(stuff)
# 用‘＃’连接stuff，起始为第四个元素，到第六个元素结束（不包含第六个元素）
print '#'.join(stuff[3:5])
