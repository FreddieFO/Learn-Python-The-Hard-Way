# this imports argv features from sys modules (why we're able to call open() and .read())
from sys import argv
# this lets user to input their argument variables which we call on later
 script, filename = argv
# this uses the built-in open function to open the file the user chooses
txt = open(filename)
# this displays the filename and uses the txt.read() to display content from the file
print "Here's your file %r:" % filename
print txt.read()
# This is the same process as above but with raw_input
filename = open(raw_input("Name of file: "))
# txt = open(filename)
print "Here's the file:"
print filename.read()
filename.close()