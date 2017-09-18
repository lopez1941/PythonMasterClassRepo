# dictionaries- unordered collections, sets- similar to lists, unordered, can't access individual items
# dictionaries- key ordered pairs

# fruit = {"orange": "a sweet orange citrus fruit",
#          "apple": "good for making cider",
#          "lemon": "a sour yellow citrus fruit",
#          "grape": "a small, sweet fruit growing in bunches",
#          "lime": "a sour, green citrus fruit"}
# print(fruit)
# print(fruit["orange"])  # access elements like a list with []
# print(fruit["lime"])
#
# # how to add to dictionaries
# fruit["pear"] = "an odd shaped apple"
# print(fruit)  # key names are/have to be unique.  if you try to add another with the same name, it will just overwrite
# # the existing one
# fruit["pear"] = "sometimes good, sometimes crap"
# print(fruit)
# print(fruit["pear"])

# to delete an item from a dictionary, use the del command
# del fruit["lemon"]  # if you forget to supply a key, 'lemon' in this case, it will delete the entire dictionary
# print(fruit)

# if you want to keep the fruit dictionary, but empty out its contents
# fruit.clear()
# print(fruit)
#
# print(fruit["tomato"])

fruit = {"orange": "a sweet orange citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

# get method of a dictionary retrieves a value for a specified key
# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#     if dict_key in fruit:
#         description = fruit.get(dict_key)
#         print(description)
#     else:
#         print("we don't have a " + dict_key)

# can also do it this way:

# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#     description = fruit.get(dict_key, "We don't have a " + dict_key)
#     print(description)

# for i in range(10):
#     for snack in fruit:
#         print(snack + " is " + fruit[snack])
#     print('-' * 40)

# ordered_key = list(fruit.keys())
# ordered_key.sort()
# ordered_keys = sorted(list(fruit.keys()))
# for f in ordered_keys:
#     print(f + "- " + fruit[f])

# for f in sorted(fruit.keys()):
#     print(f + '- ' + fruit[f])

# for val in fruit.values():
#     print(val)
# print("-----")
# for key in fruit:
#     print(fruit[key])

# fruit_keys = fruit.keys()
# print(fruit_keys)
# fruit["tomato"] = "not nice with ice cream"
# print(fruit_keys)

print(fruit)
print(fruit.items()) # looks like a tuple
fruit_tuple = tuple(fruit.items())
print(fruit_tuple)
# once it's a tuple, you can unpack it
for snack in fruit_tuple:
    item, description = snack
    print(item + " is " + description)
# can also make a tuple a dictionary with dict
print(dict(fruit_tuple))
