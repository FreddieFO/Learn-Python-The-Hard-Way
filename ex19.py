# we DEFINE a function here, it contains two arguments and 4 print statements
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket. \n"

# we call on the function and pass numbers as the arguments
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# we call the function again, passing variables as it's arguments
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# we call the function, giving it numbers which use math
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# we call the function, giving it a mixture of variables and math
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


# Study Drill - my custom function
def football_score(team_a, team_b, prediction):
	print "\n So according to you, %s will beat %s by %d goals" % (team_a, team_b, prediction)
	print "Or %s will beat %s by %d? \n" % (team_b, team_a, prediction)

print "What are the teams ?"
team_1 = raw_input("First team? ")
team_2 = raw_input("Their opponent? ")
goals = int(raw_input("How many goals? ")) 

football_score(team_1, team_2, goals * 2)