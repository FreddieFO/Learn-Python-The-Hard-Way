# -*- coding: utf-8 -*-
name = 'Freddie the don'
age = 24
height = 6 # feet
weight = 86 # kg
eyes = 'Green'
teeth = 'White....DUH'
hair = 'Wavy Black'
idealweight = 10
# write variables to convert feet to centimeters and kg to stone
feet_to_cm = 30.48
kg_to_stone = 0.157473
print "Let's talk about %r." % name
print "He's %d feet tall. In cm this is %d" % (height, height * feet_to_cm)
print "He's %d kg heave. This is equivalent to %d stones" % (weight, round(weight * kg_to_stone))
print "He's aiming to gain %d kg meaning %d in stones." % (idealweight, round(idealweight * kg_to_stone))
print "He's got %s eyes and %r hair" % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth


print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
