tabby_cat = "\fI'm tabbed in." # \t means indent tab
persian_cat = "I'm split\bon a line."
backslash_cat = "I'm  a cat." +  u'\U0001F47E' 

fat_cat = '''
I'll do a list:
\v* Cat food 
\n\t\r* Fishies
\t* Catnip\n\t* Grass

'''


print tabby_cat + "I'm trying to make \n this quite complex\b ... so bare %r %s" % ("WITH", "me baybay")
print persian_cat + "%s" % u'\U0001F408'
print backslash_cat
print fat_cat
print ''' I am a fat cat %s \n somebody please help %s ''' % (u'\U0001F63F', u'\U0001F640')


#while True:
#	for i in ["/","-","|","\\","|"]:
#		print "%s\r" % i,