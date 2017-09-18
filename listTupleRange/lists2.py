# list constructor
#
# list_1 = []
# list_2 = list()  # constructs an empty list
#
# print("""List 1: {0}
# List2: {1}""".format(list_1, list_2))
#
# if list_1 == list_2:
#     print("The lists are equal")  # everything inside the '()' of the print function is an arg or parameter
# # iterable parameter- object capable of returning its members one at a time
# # below will add the string contents individually to a list and print them separately
# print(list("The lists are equal"))  # list function" list() " constructs or creates a list

# both lists will point to the same data in memory
# even = [2, 4, 6, 8]
# anotherEven = even
# anotherEven.sort(reverse=True)
# print(even)
# print(anotherEven)
# print(anotherEven is even)
#
# # list constructor actually creates a new list so eval will return false though the values are the same
# anotherEven = list(even)
# print(even)
# print(anotherEven)
# print(anotherEven is even)
# # the contents are ==, but the objects in memory aren't the same as they are in
# # the previous example
# print(anotherEven == even)

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
# appends the two separate lists into a new list called numbers
numbers = [even, odd]
print(numbers)

for number_set in numbers:
    print(number_set)

    for value in number_set:
        print(value)
