days = "Mon Tue Wed Thu Fri Sat Sun"
# I think \n means new line
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
# using comma then a variable seems to give the same effect as using a fromatter at the end of a sentence
print "Here are the days: ", days
print "Here are the months: ", months
# Using three quotes let's you type your string output without putting print in front of every line
# it also creates a space before an dafter the output
print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, 5, or 6.
"""