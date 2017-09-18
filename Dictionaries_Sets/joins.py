myList = ["a", "b", "c", "d"]
# strings are immutable. adding in a loop causes it to create a new variable each loop through
# newString = ''
# for c in myList:
#     newString += c + ", "
# print(newString)

#  better way to do it is:
newString = ", ".join(myList)
print(newString)

newString = ''
letters = "abcdefghijklmnopqrstuvwxyz"
newString = ",".join(letters)
print(newString)

numbers = "1234567890"
newstring = " mississippi ".join(numbers)
print(newstring)

