# a set is unordered and doesn't contain duplicates
# items aren't accessed by a key
# supports union and intersection operations

# farm_animals = {"sheep", "cow", "hen"}
# print(farm_animals)
#
# for animal in farm_animals:
#     print(animal)
#
# print("=" * 40)
#
# wild_animals = set(["lion", "tiger", "panther", "elephant", "hare"])
# print(wild_animals)
#
# for animal in wild_animals:
#     print(animal)
#
# farm_animals.add("horse")
# wild_animals.add("horse")
#
# print(farm_animals)
# print(wild_animals)
#
# empty_set = set()
# empty_set2 = {}
# empty_set.add("a")
# #empty_set2.add("a")
#
# even = set(range(0, 40, 2))
# print(even)
#
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print(squares)

# even = set(range(0, 40, 2))
# print(even)
# print(len(even))
#
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print(squares)
# print(len(squares))
#
# print(even.union(squares))  # joins both together without duplicates
# print(len(even.union(squares)))
#
# print("-"  * 40)
# print(even.intersection(squares))  # finds what's in both without duplicates
# print("-"  * 40)
# print(squares.intersection(even))
# print(squares & even)

# subtracting: set A minus set b will subtract any item in A that exists in set b

# even = set(range(0, 40, 2))
# print(sorted(even))
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print(sorted(squares))
# print("even minus squares")
# print(sorted(even.difference(squares)))
# print(sorted(even - squares))
#
# print("squares minus even")
# print(sorted(squares.difference(even)))
# print(sorted(squares - even))
#
# print("=" * 40)
# print(sorted(even))
# print(squares)
# even.difference_update(squares)  # performs an in place subtraction on the 'even' set, doesn't actuallly output anything
# print(sorted(even))

# even = set(range(0, 40, 2))
# print(sorted(even))
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print(sorted(squares))

# gives everything but what's in common
# print("symetric even minus squares")
# print(sorted(even.symmetric_difference(squares)))  # all members in one or the other, but not both
# print("symetric squares minus even")
# print(sorted(squares.symmetric_difference(even)))

# to remove items from a set, use discard or remove
# remove will raise an error if an item doesn't exist, discard won't

# squares.discard(4)
# squares.remove(16)
# squares.discard(8)
# print(squares)
# # squares.remove(8)  error because 8 isn't in there
# try:
#     squares.remove(8)
# except KeyError:
#     print("item 8 is not a member of the set")

# even = set(range(0, 40, 2))
# print(even)
# squares_tuple = (4, 6, 16)
# squares = set(squares_tuple)
# print(squares)
#
# if (squares.issubset(even)):
#     print("Squares is a subset of even.")
# if even.issuperset(squares):
#     print("Even is a superset of squares.")

# sets aren't used as much as lists or dictionaries
# a frozen set is an immutable set (can't be modified or changed)
even = frozenset(range(0, 100, 2))
print(even)
#even.add(3)  # errors out because you can't add to a frozenset
otherEven = frozenset(range(0, 40, 2))
print(otherEven)
print(even - otherEven)  # you can still do functions on them
otherBigEven = frozenset(range(100, 200, 2))
combinedSet = even.union(otherBigEven)
print(combinedSet)


