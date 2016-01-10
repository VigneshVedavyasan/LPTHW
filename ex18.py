#this one is like your scripts with argv

def print_two(*args):
    arg1,arg2=args
    print "arg1: %r, args2: %r" %(arg1, arg2)

#ok that *args is pointless we can do this!   
def print_two_again(arg1,arg2):
    print "arg1: %r, args2: %r" %(arg1,arg2)
    
def print_one(arg1):
    print "arg1: %r"%arg1
    
def print_none():
    print "I got nothing"
    
print_two("Make","Two")
print_two_again("Making","Twice")
print_one("Make")
print_none()
