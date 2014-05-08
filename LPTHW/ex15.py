# sys built-in module provides access to some objects used or maintained by the
# interpreter and to functions that interact strongly with the interpreter
# argv is a dynamic object that requests command line arguments
# For now just understand that sys is a package, 
#  and this phrase just says to get the argv feature from that package. 
from sys import argv

script, filename = argv # requires theses 2 command line arguments

# open() method opens a file using the file() type, returns a file object 
# Like raw_input(), it takes a parameter and returns a value you can set to own variable
# Doesn't return contents file, instead makes something called a "file object" 
txt = open(filename)

# After open() returns files it contains methods like the .read() function
# We can give files a command with "." + name of command + parameters
# txt.read() means "Hey txt! Do your read command with no parameters!"
print "Here's your file %r:" % filename
print txt.read()

# another way of getting the file name from user w/o req. command line argv
print "Type another filename:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()