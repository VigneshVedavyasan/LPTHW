from sys import argv
script,filename=argv

print "Lets open a file."
txt_file=open(filename)

print "Here is the file %r\n" %filename
print txt_file.read()

print "Lets open the file again."
print "Enter filename again.\n"
file_name=raw_input('> ')

txt_file_again=open(file_name)

print "File opened again.\n"
print txt_file_again.read()

txt_file.close()
txt_file_again.close()

