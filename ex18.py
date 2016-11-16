# this is like the scripts with argv
# the * tells python to take all the arguments to the function and put them in args as a list
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# same as above but without the *args
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# this takes just one argument
def print_one(arg1):
	print "arg1: %r" % arg1

# this takes no arguments
def print_none():
	print "I got nothin'."


print_two("Fred","Oduks")
print_two_again("Fred", "Oduks")
print_one("First!")
print_none()