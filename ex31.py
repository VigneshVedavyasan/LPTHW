print "You enter a dark room with two doors. Do you go through door #1 or door #2?"
door=raw_input("> ")

if door=="1":
    print "There is a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."
    
    bear=raw_input("> ")
    
    if bear=="1":
        print "The bear eats you face off. Good Job!"
    elif bear=="2":
        print "The bear eats your legs off. Good Job!"
    else:
        print "Well, doing %s is probably better. Bear runs away." %bear
elif door=="2":
    print "You stare into the endless abyss at C'Thun's retina."
    print "1. You think its blueberries"
    print "2. You think it is a front-load washing machine and put you clothes in it"
    print "3. You poke by kicking its retina."
    insanity=raw_input("> ")
    
    if insanity=="1":
        print "You are devoured by C'Thun."
    elif insanity=="2":
        print "You got some sense of humor. But you hurt C'Thun's eyes and you should make a run for it. You fall and hurt your leg but still survive."
    elif insanity=="3":
        print "You got guts! You fall down and hurt your leg but remain alive you can run away to save yourself!"
    else:
        print "You are deeply hipnotised by the ocular power of C'Thun. It does unimaginable things to you and you are devoured with very very less honor! So sorry!"
else:
    print "You stumble around, fall on a knife and die!. Good Job =<"
