from sys import argv
script,filename=argv
print "We are deleting contents of %r." %filename
print "If you wish to stop it hit 'CTRL+C'."
print "If you wish to continue hit 'RETURN'."

raw_input("? ")
print "Opening the file..."
target=open(filename,'w')
print "Deleting... Good Bye!\n"
#target.truncate()
print "The file now has..."
getting=open(filename)
print getting.read()

print "Now We are going to Write 3 lines to the file."

line1=raw_input("Line 1: >")
line2=raw_input("Line 2: >")
line3=raw_input("Line 3: >")
full_txt=line1+'\n'+line2+'\n'+line3

print "Writing..."

target.write(full_txt)


print "And finally, we close it."
target.close()
