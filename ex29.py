people = int(raw_input("How many people exist? "))
cats = int(raw_input("How many cats exist? "))
dogs = int(raw_input("How many dogs exist? "))


if people < cats:
	print "Too many cats! The world is doomed!"

if people != cats:
	print "Not many cats! The world is saved!"

if people < dogs:
	print "The world is drooled on!"

if people > dogs:
	print "The world is dry!"


dogs += 5

if people >= dogs:
	print "People are greater than or eual to dogs."

if people <= dogs:
	print "People are less than or equal to dogs."


if people == dogs:
	print "People are dogs."

#if statement creates a branch in the code. The if the boolean exression in the
# code is true then the script will run the code under the statement otherwise ignore

#if needs to be intended so python recognises you're creating a new block of code. The
# indentaion only comes after the colon at the end of the function name line.