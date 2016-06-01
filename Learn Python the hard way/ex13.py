# -*- coding: utf-8 -*-

from sys import argv

# 将argv中的东西解包，所有的参数依次赋值给左边的变量
script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is", second
print "Your third variable is:", third