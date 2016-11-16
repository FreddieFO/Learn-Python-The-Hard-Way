# Import the argv methods from the sys module
from sys import argv

# -*- coding: <UTF-8> -*-

# assign the chosen script and filename as argument variables
script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")
# opens chose file and lets it know we can write in this file. Then assign it
# to a variable 
print "Opening the file..."
target = open(filename, 'w')
# empties the file
print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."
# gets new text from user
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ") 
final_line = line1 + "\n" + line2 + "\n" + line3 + "\n" 
print "I'm going to write these to the file."
# writes the text user entered from lines 21 to 23.
target.write(final_line)
# closes and saves the file
print "And finally, we close it."
target.close()