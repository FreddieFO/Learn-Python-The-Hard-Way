# this imports modules from sys (why we're able to call open() and .read())
from sys import argv
# this lets user to input their argument variables which we call on later
script, filename = argv
# this uses the built-in open function to open the file the user chooses
txt = open(filename)
# this displays the filename and uses the txt.read() to display content from the file
print "Here's your file %r:" % filename
print txt.read()
# this is the same process as that above
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()