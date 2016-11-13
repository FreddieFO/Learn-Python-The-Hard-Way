from sys import argv

script, user_name, nick_name = argv
prompt = '--> '

print "Hi %s or do you prefer %s?, I'm the %s script." % (user_name, nick_name,
	script)
preferred_name = raw_input("Your name preference? ")
print "Ok I'll call you %s" % preferred_name

print "I'd like to ask you a few questions."
print "Do you like me %s?" % preferred_name
likes = raw_input(prompt)

print "Where do you live %s?" % preferred_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice bro!.
""" % (likes, lives, computer)