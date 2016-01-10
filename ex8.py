formatter="%r %r %r %r"

superb="%s %d %r"

print formatter%(1,2,3,4),
print formatter%('one','two','three','four')
print formatter%(True,False,False,True)
print formatter%(superb,superb%('supe',10,20),formatter,formatter%('ilike','tasty',20,20))
print formatter%("I had this thing.", "That you could type up right.","But it didn't sing.","So I said goodnight.")
