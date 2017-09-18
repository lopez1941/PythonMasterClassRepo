menu = []
menu.append(["egg", "spam", "bacon"])
menu.append(["egg", "sausage", "bacon"])
menu.append(["egg", "spam"])
menu.append(["egg", "bacon", "spam"])
menu.append(["egg", "bacon", "sausage", "spam"])
menu.append(["spam", "bacon", "sausage", "spam"])
menu.append(["spam", "egg", "spam", "spam", "bacon", "spam"])
menu.append(["spam", "egg", "sausage", "spam"])

#print(menu)

# for meal in menu:
#     if not "spam" in meal:
#         print(meal)
# challenge is to add to the program, find a meal that doesn't have 'spam' in it,
# and then print the individual components of the meal, rather than the list as a whole

for meal in menu:
    if not "spam" in meal:
        for item in meal:
            print(item)
# nailed it!
