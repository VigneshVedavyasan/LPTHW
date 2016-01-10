def cheese_and_crackers(cheese_count,boxes_of_crackers):
    print "You have got %d cheese."%cheese_count
    print "You have got %d boxes of crackers."%boxes_of_crackers
    print "Man thats enough for the party."
    print "Get a blanket."

print "We can give the function values directly."
cheese_and_crackers(20,30)

print "Or we can use variable names to assign to function arguments."
amount_of_cheese=10
amount_of_crackers=50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print "We can even do math inside too: "
cheese_and_crackers(10+20,5+6)

print "And we can combine two, variables and math:"
cheese_and_crackers(amount_of_cheese +100,amount_of_crackers+1000)

print "Finally we can get input from the user > "
amount_of_cheese=raw_input("> ")
amount_of_crackers=raw_input("> ")
cheese_and_crackers(int(amount_of_cheese),int(amount_of_crackers))
