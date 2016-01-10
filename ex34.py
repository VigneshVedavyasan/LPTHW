animals=['bear','python','peacock','kangaroo','whale','platypus']
print "Do you want to know the index of an animal or get animal from an index value\n1.Index\n2.Animal\n"
index=raw_input("> ")
j=0
r=0
if index=="1":
    print "Enter the index value >"
    ind=int(raw_input())
    for i in animals:
        j=j+1
        if j==ind:
            print i
            break
elif index=="2":
    print "Enter the animal's name: "
    name=raw_input()
    for n in animals:
        r=r+1
        if n==name:
            print r
else:
    print "You didn't enter valid values"    
