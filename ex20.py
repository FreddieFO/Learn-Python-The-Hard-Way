from sys import argv

script, input_file = argv
# define a function that reads the file
def print_all(f):
	print f.read()
# define a functions that rewinds(?) the file
# seek(0) moves you back to the start of the file. deals in bytes not lines
def rewind(f):
	f.seek(0)
# define a function that scans each byte of the file until it finds \n and displays the
# line number
def print_a_line(line_count, f):
	print line_count, f.readline(),
# opens our input file
current_file = open(input_file)

print "First let's print the whole file:\n"
# reads the file using print all function
print_all(current_file)

print "Now let's rewind, kind of like a tape."
# rewinds (?) the file 
rewind(current_file)

print "Let's print three lines:"
# prints the current line (line 1) of the input file and prints it
current_line = 1
print_a_line(current_line, current_file)
# prints the current line + 1 (line 2) of the input file and prints it
current_line += 1
print_a_line(current_line, current_file)
# same as above
current_line += 1
print_a_line(current_line, current_file)