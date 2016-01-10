#create a mapping of state to abbreviation

states={
    'Tamil Nadu': 'TN',
    'Karnataka': 'KA',
    'Goa': 'GA',
    'Odisha': 'OR',
    'Andra Pradesh': 'AP'
    }
#create a basic set of states and some cities in them
cities={
    'GA': 'Panaji',
    'AP': 'Hyderabad',
    'OR': 'Bhubaneswar'
    }
#add some more cities
cities['KA']='Mysuru'
cities['TN']='Coimbatore'
#print out some cities
print '=-'*20
print "TN State has: ",cities['TN']
print "KA State has: ",cities['KA']
#print some states
print '=-'*20
print "Andra Pradesh's abbreviation is: ",states['Andra Pradesh']
print "Tamil Nadu's abbreviation is: ",states['Tamil Nadu']
#Do it by using the state then cities dict
print "=-"*20
print "Tamil Nadu has: ",cities[states['Tamil Nadu']]
print "Karnataka has: ",cities[states['Karnataka']]
#print every state abbreviation
print "=-"*20
for state,abbrev in states.items():
    print "%s is abbreviated %s" %(state,abbrev)
#print every city in state
print "=-"*20
for abbrev,city in cities.items():
    print "%s has the city of %s"%(abbrev, city)
#now do both at the same time
print "=-"*20
for state,abbrev in states.items():
    print "%s state is abbreviated %s and has city of %s"%(state,abbrev,cities[abbrev])

print "=-"*20
#safely get a abbreviation by state that might not be there
new_state='Telangana'
state=states.get(new_state)
if not state:
    print "Sorry no %s"%new_state
#get a city with a default value
city=cities.get('TG','Doesn\'t exists')
print "The city for the state 'TG' is : %s" %city
