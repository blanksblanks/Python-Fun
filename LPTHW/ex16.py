from sys import argv

script, filename = argv

print "We're going to rewrite %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w') # opens this file explicitly in "write" mode
print "Truncating the file. Goodbye!"
target.truncate() # empties the file out, doesn't appear necessary though

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ") # allows user to type after line 1:
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file"

# writes new content in the file with line breaks and new line at end
target.write("%s\n%s\n%s\n" % (line1, line2, line3))

# above used to be six lines, but formats and escapes helped me make it one
# note that % (line1...) HAS to be inside write function otherwise you will get error
# also note no spacing between \n unless you want each line to start with spaces
# and the error will be after you run the code, not before it

print "And finally, we close it."
target.close() # closes file so that changes can be saved

# run in python as txt = open("test.txt)
# followed by print txt.read() to see new contents

