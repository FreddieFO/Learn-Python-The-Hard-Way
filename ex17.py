from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)
# this is bad practice? I should close it myself?
indata = open(from_file).read(); # indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)


out_file = open(to_file, 'w'); out_file.write(indata)

print "Alright, all done."
# we have to close this file in order to save the changes but if we use open(f).read()
# then we don't need to close it
# out_file.close(); in_file.close()