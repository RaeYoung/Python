from sys import argv

script, filename = argv

#open the file named filename, retures the file objext to variable txt.
txt = open(filename)

print "Here's your file %r" % filename
#read the file and print it's content. read() is a method to the file.
print txt.read()
txt.close()

print ("Type the filename again:")
file_again = raw_input("> ")

txt_again = open(file_again)
print txt_again.read()
txt_again.close()
