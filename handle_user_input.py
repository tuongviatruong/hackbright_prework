# Handle User Input
first_name = raw_input("What's your first name?")
last_name = raw_input("What's your last name?")
fav_color = raw_input("What's your favorite color?")
num_pets = raw_input("How many pets do you have?")

print "Great! So your name is {} {}, your favorite color is {} and you have {} pets. Nice to meet you!".format(first_name,last_name,fav_color,num_pets)

# Formatting text
paragraph = """An invitation to dinner was soon afterwards dispatched;
and already had Mrs. Bennet planned the courses that were to do credit
to her housekeeping, when an answer arrived which deferred it all. Mr.
Bingley was obliged to be in town the following day, and, consequently,
unable to accept the honour of their invitation, etc. Mrs. Bennet was
quite disconcerted."""

average_rating = 4.56789123
average_rating = str(average_rating)

print paragraph[:10] + "..."
print average_rating[:4]

# Discussion Question
#it is invalid because Python doesn't do replacement. Strings are immutable.