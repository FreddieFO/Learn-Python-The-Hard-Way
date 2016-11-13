#We assign a string to a variable here, in this case using the %d formating string which lets us put single digit integers
x = "There are %d types of people." % 10
# strings are siigned to variables
binary = "binary"
do_not = "don't"
# when using multiple format char's and  variables, parentheses are placed around the variables
y = "Those who know %s and those who %s." % (binary, do_not)
# display the variables
print x
print y
#display a string which contains variables generated above
print "I said: %r." % x
print "I also said: '%s'." % y
# assign a boolean to a variable
hilarious = False
# assign a string containing a format character to be used later
joke_evaluation = "Isn't that joke so funny?! %r"
# display both variables. the %r char placed in the joke_eval var works with the hilarious var placed after the %
print joke_evaluation % hilarious
# assign strings to variables and print them together to create a longer string
w = "This is the left side of..."
e = "a string with a right side."

print w + e