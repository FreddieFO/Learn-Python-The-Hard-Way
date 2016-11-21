def add(a, b):
	print "Adding %d + %d" % (a, b)
	return a + b

def subtract(a, b):
	print "Subtracting %d - %d" % (a, b)
	return float(a) - float(b)

def multiply(a, b):
	print "Multiplying %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "Dividing %d / %d" % (a, b)
	return a / b


print "Let's do math with just functions!"

age = add(float(raw_input("first number to add?")), float(raw_input("Second number?")) )
height = subtract(50.7, 2.5)
weight = multiply(17, 23)
iq = divide(343, 33)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)



print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"