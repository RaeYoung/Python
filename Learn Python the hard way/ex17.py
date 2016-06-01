# -*- coding: utf-8 -*-
from sys import argv
# exists命令将文件名字符串作为参数，若文件存在，返回true， 反之返回false
from os.path import exists

script, from_file, to_file = argv

#用这种方式，不用再用close， 因为python在read运行会关闭文件
indata = open(from_file).read()

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

#同样的，运行完自动关闭文件
out_file = open(to_file, 'w').write(indata)

print "Alright, all done."
