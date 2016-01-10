from sys import argv

script,filename=argv

txt=open(filename)
print "contents..\n"+txt.read()
txt.close()

print "Deleting..."
txt=open(filename,'w')
txt.close()

print "Contents now"
txt=open(filename)
print '\n'+txt.read()

print "Type in filename to be copied"
file2=raw_input("> ")
txt2=open(file2)

copier=txt2.read()
print "Content of source :\n"+copier+'\n'

txt=open(filename,'w')
txt.write(copier)
txt.close()
txt=open(filename)
print "Contents copied.\n"+txt.read()

txt.close()
txt2.close()
