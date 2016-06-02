# -*- coding: utf-8 -*-
from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print("Opening the file...")
#以可写的方式打开文件
target = open(filename, 'w')

print "Truncating the file.  Goodbye!"
#在写入之前清空文件
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1+"\n"+line2+"\n"+line3) 

print "And finally, we close it."
target.close()
