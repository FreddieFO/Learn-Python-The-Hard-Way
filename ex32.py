the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this for-loop goes through a list
for number in the_count:
	print "This is count %d" % number

# same as above
for fruit in fruits:
	print "A fruit of type: %s" % fruit

# when going through mixed lists, use %r as we don't know whats in it
for i in change:
	print "I got %r" % i 



elements = []

# the range function will do 0 to 5 counts
for i in range(0, 7):
	print "Adding %d to the list." % i
	# append is a function that lists understand
	elements.append(i)


for i in elements:
	print "ELements was: %d" % i

print list( (0, 1, 2, 3, 4) )