# no. of cars present
cars = 100
# no. of seats in any car. 4.0 is a floating point number meaning it has a decimal point
space_in_a_car = 4.0
# people available to drive said cars
drivers = 30
# people being driven
passengers = 90
#leftover cars
cars_not_driven = cars - drivers
#cars being used
cars_driven = drivers
# total amount of possible people to be transported
carpool_capacity = cars_driven * space_in_a_car
# average no. of passengers per car 
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
print "Hey %s there." % "you"