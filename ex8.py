# A string of string format char's is assigned to a variable
formatter = "%r %r %r %r"
# The output shows the raw format (from the formatter var) of the assigned values in the parantheses
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
# This line prints all but one of the values in parentheses in single quotes, why?ß
# the 3rd line contains a single quote("didn't") so python assigned it double quotes
print formatter % (
	"I had this thing.",
	"That you could type right.",
	"But it didn't sing.", 
	"So I said goodnight."
	)