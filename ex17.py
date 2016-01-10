from sys import argv
from os.path import exists

script,from_file,to_file=argv
print "Transfering data from %r to %r."%(from_file,to_file)

in_file=open(from_file)
indata=in_file.read()

print "The input file is %d bytes long."%len(indata)

print "Does the output file exist? %r"%exists(to_file)
print "Hit CTRL+C to abort or RETURN to continue.\n"
raw_input("> ")

out_file=open(to_file,'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()
