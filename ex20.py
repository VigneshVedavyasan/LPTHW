from sys import argv
script, input_file=argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)
    
def print_in_a_line(line_count,f):
    print line_count, f.readline()
    
current_file=open(input_file)

print "Lets first print the whole file \n"
print_all(current_file)

print "Lets reset the position of the file object reference variable :"
rewind(current_file)

print "Lets print three line one by one. "
current_line=1
print_in_a_line(current_line,current_file)

current_line=current_line+1
print_in_a_line(current_line,current_file)

current_line=current_line+1
print_in_a_line(current_line,current_file)    
