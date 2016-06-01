# -*- coding: utf-8 -*-
#声明字符串变量（涉及格式化字符），可直接引用，也可间接引用变量
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

#
print "I said: %r." % x
print "I also said: '%s'." % y


hilarious = True
#声明变量时便引入格式化字符，打印时再添加%符号
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

#使用＋号连接两个字符串，无空格
print w + e