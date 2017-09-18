# Write a small program to ask for a name and an age.
# When both values have been entered, check if the person
# is the right age to go on an 18-30 holiday (they must be
# over 18 and under 31).
# If they are, welcome them to the holiday, otherwise print
# a (polite) message refusing them entry.

guestName = input("Hello.  What is your name? ")
guestAge = int(input("Hello {0}. How old are you? ".format(guestName)))

if 18 <= guestAge <= 30:
    print("Very well!  Welcome aboard {0}, to your awesome holiday!".format(guestName))
elif guestAge < 18:
    print("Oh, I'm sorry {0}.  Guests must be between the ages of 18 and 30 for this trip. :-(".format(guestName))
    print("Please come back in {0} years.".format(18 - guestAge))
else:
    print("I'm sorry {0}.  We're not sure this holiday is a good fit for you.".format(guestName))

