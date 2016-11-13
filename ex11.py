print "What's your name?",
name = raw_input('-->')
print "How old are you %s?" % name,
age = int(raw_input()) # int converts the string from the raw_input and converts it to an integer
print "How tall are you %s?" % name,
height = int(raw_input())
print  "What team do you suport %s?" % name,
team = raw_input()

print "So, you're %r old, %r tall and support %r." % (age, height,
	   team)

print " Hello %s, Let's play a math game" % name
print "Choose a number from 1 - 10",
intial_no = int(raw_input('-->'))
new_no = intial_no + 10
print "Add 10 to the number, the answer should be = %r" % new_no 

