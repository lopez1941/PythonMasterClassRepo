# sometimes you need to interrupt the flow of a loop

# shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
# for item in shopping_list:
#     print("Buy this: " + item)
#
# shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
# for item in shopping_list:
#     if item == 'spam':
#         print("I'm ignoring " + item + "!")
#         continue  # continue stops it from processing, and goes to the next item
#                   # this effectively skips 'spam
#     print("Buy: " + item)
#
# for item in shopping_list:
#     if item == 'spam':
#         print("I'm ignoring " + item + "!")
#         break  # break busts out of the loop completely and doesn't continue
#     print("Buy: " + item)

# meal = ["eggs", "bacon", "spam", "sausages"]
# nasty_food_item = ''
# for item in meal:
#     if item == "spam":
#         nasty_food_item = item
#         break  # use break to terminate a loop early when a condition is met
#
# if nasty_food_item:
#     print("Can I have something without spam please?")

meal = ["eggs", "bacon", "beans", "sausages"]  # change beans to spam and vice versa
nasty_food_item = ''  # can use underscores or camel case for variables
item = ''

for item in meal:
    if item == "spam":
        nasty_food_item = item
        break  # use break to terminate a loop early when a condition is met
else:
    print("I'll have a plate of {0} please.".format(item))
if nasty_food_item:
    print("Can I have something without spam please?")
