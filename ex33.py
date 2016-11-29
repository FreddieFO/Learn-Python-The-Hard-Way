def while_loop(i, num, delta):
	""" This function runs a while loop that appends your chosen numbers to a list"""
	numbers = []
	while i < num:
		print "At the top i is %d" % i
		numbers.append(i)

		i += delta
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

	print "The numbers: "

	for digits in numbers:
		print digits
# this for loop below was designed to replicate the while loop above, it is my
# intepretation of the study drill
def for_loop(x, y, z):
	""" This function runs a for loop that appends your chosen numbers to the list."""
	numbers = []
	for i in range(x, y, z):
		print "At the top i is %d" % i
		numbers.append(i)

		bottom = i + z
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % bottom 

	print "The numbers: "

	for digits in numbers:
		print digits
