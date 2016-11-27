people = int(raw_input("No. of People? "))
cars = int(raw_input("No. of Cars? "))
trucks = int(raw_input("No. of trucks? "))


if cars > people and people < trucks or trucks > cars:
	print "We should take the cars."
elif cars < people or cars > trucks or people > trucks:
	print "We should not take the cars but take the trucks."
else:
	print "We can't decide."

#if trucks > cars:
#	print "That's too many trucks bruh!."
#elif trucks < cars:
#	print "Maybe we could take the trucks"
#else:
#	print "We still can't decide."

#if people > trucks:
#	print "Alright, let's just take the trucks."
#else: 
#	print "Fine, let's stay home then."
