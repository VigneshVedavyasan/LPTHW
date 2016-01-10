def add(arg1,arg2):
    print "Adding %d and %d :"%(arg1,arg2)
    return arg1+arg2

def subtract(arg1,arg2):
    print "Subtracting %d by %d :"%(arg1,arg2)
    return arg1-arg2
    
def multiply(arg1,arg2):
    print "Multiplying %d with %d :"%(arg1,arg2)
    return arg1*arg2

def divide(arg1,arg2):
    print "Dividing %d by %d :"%(arg1,arg2)
    return arg1/arg2
    
age=add(20,7)
height=subtract(200,20)
weight=multiply(10,8)
iq=divide(200,2)

print " Age : %d,\n Height : %d\n Weight : %d\n IQ : %d"%(age,height,weight,iq)

print "We can do this too!"
new_val=add(age,subtract(height,multiply(weight,divide(iq,2))))
print "This is : %d"%new_val
