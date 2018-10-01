print "Welcome to Build-A-Bear!"
user = raw_input("What's your name? ")
user = user.capitalize()

print "Hi {}, please choose a stuffed animal ".format(user)
print "a. Color Craze Unicorn"
print "b. Black Panther Bear"
print "c. Bright Blue Bunny"
print "d. Smiley Monkey"
print "e. Wild Style Giraffe"
animal = raw_input( ">>")
animal=animal.lower()

if animal == "a":
    print "Great! You got a Color Craze Unicorn."
elif animal == "b":
    print "Great! You got a Black Panther Bear."
elif animal == "c":
    print "Great! You got a Bright Blue Bunny."
elif animal == "d":
    print "Great! You got a Smiley Monkey."
elif animal == "e":
    print "Great! You got a Wild Style Giraffe."
else:
    print "Please choose only from a-e"

print "What do you want to name it?"
name = raw_input(">>")
name = name.capitalize()
    
print "Now you can select a sound chip so {} can make a sound or speak".format(name)
print "What do you want {} to say?".format(name)

print "a. 'I Love You'"
print "b. Growl"
print "c. Giggle"
print "d. Star Wars Theme Song"
print "e. Silly Burp Sounds"

sound = raw_input(">>")
sound = sound.lower()

if sound == "a":
    print "Awesome! Now {} can say I Love You!".format(name)
elif sound == "b":
    print "Awesome! Now {} can growl".format(name)
elif sound == "c":
    print "Awesome! Now {} can giggle".format(name)
elif sound == "d":
    print "Awesome! Now {} can have the Star Wars Theme Song".format(name)
elif sound == "e":
    print "Awesome! Now {} will have silly burp sounds".format(name)
else:
    print "Please choose only from a-e"

print "You can choose a scent disk so {} can have a smell.".format(name)
print "What do you want {} to smell like?".format(name)

print "a. Bubblegum "
print "b. Chocolate "
print "c. Lavender"
print "d. Strawberries"

smell = raw_input(">>")
smell = smell.lower()

if smell == "a":
    print "Sweet, now {}'s paw can smell like bubblegum".format(name)
elif smell == "b":
    print "Sweet, now {}'s paw can smell like chocolate".format(name)
elif smell == "c":
    print "Sweet, now {}'s paw can smell like lavender".format(name)
elif smell == "d":
    print "Sweet, now {}'s paw can smell like Strawberries".format(name)
else:
    print "Please choose only from a-e"

print
print
print "Great! Now we will put a heart in {} and it will now be stuffed! ".format(name)
print
print "....."
print "....."
print "stuffing"
print "...."
print "...."
print "Done!"
print
print
print "This is {}'s birth certificate:".format(name)
print "Name: {}".format(name)
print "Height: 18 inches"
print "Weight: 8 ounces"
print "Eye Color: Black"
print "Belongs to: {}".format(user)
    





