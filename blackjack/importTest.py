#  the way import works, is when it finds the module or file you import, it immediately runs it

# convention is to add a single underscore to a variable name if it would conflict with a python builtin
#  python has no notion of private variables
# starting a function name with an '_' indicates that it should be treated as private, but nothing in the language
# itself will force that on you.  it will warn you, but allow you to do silly things
# if something starts and ends with '__', don't mess around with it
# variable named '_' is convention for a throw away variable, see personal details tuple below

import importminiChallenge


# importminiChallenge._deal_card(importminiChallenge.dealer_card_frame)
# importminiChallenge.play()

personal_details = ("Donnie", 37, "USA")
name, _, country = personal_details
print(name, country)
