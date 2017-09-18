# an iterator is an object that represents a stream of data, it returns the stream or data in the stream
# one value at a time

myString = "1234567890"
for char in myString:
    print(char)
# there's an iterator created from the string, and the for loop uses the iterator to return
# each value in the string

myIterator = iter(myString)
print(myIterator)
print(next(myIterator))
print(next(myIterator))
# to run through the whole list
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
# the for loop, does all this automatically
