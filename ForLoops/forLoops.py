# takes a range of values, assigns it to a variable, executes block of code for each value

# for i in range(1,20):
#     print("i is now {0}".format(i)) # last value isn't included, first number starts with 0
#     # i stands for index, and is acceptable in a for loop
#
# numberString = "0,223,372,036,854,775,807"
# for i in range(0, len(numberString)):  # len returns length of a string
#     print(numberString[i])

# print(len(numberString))

# to only print the numbers and not the commas:
# number = "0,223,372,036,854,775,807"
# for i in range(0, len(number)):  # len returns length of a string
#     if number[i] in '0123456789':
#         print(number[i],end='')  # python auto adds endline char, adding end changes the newline default
#
# number = "0,223,372,036,854,775,807"  # this 'number' is actually a string
# cleanedNumber= ''  # this variable will be used to hold the new string without the commas
#                    # it's empty right now
# for i in range(0, len(number)):  #start at position 0 and go through the entire string
#     if number[i] in '0123456789':
#         cleanedNumber = cleanedNumber + number[i]  # number cleaned of commas. cleanedNumber is still a string at this point
#
# newNumber = int(cleanedNumber)  # casting cleanedNumber as an integer
# print("The number is {0}".format(newNumber))
#

# reminder, in python a for loop- a variable interates through a series of values
# for i, iterate through the sequence and do something

number = "9,223,372,036,854,775,807"  # this 'number' is actually a string
cleanedNumber= ''

for char in number: # using char in this case as i is really for a number index
    if char in '0123456789':
        #  print(char)
        cleanedNumber = cleanedNumber + char

newNumber = int(cleanedNumber)
print("the number is {0}.".format(newNumber))

for state in ["not pining","no more","a stiff","bereft of life"]:  # iterating through one element at a time
    print("This parrot is " + state) # can use '+' here because you're concatinating strings
    # could also use replacement fields {} with .format(state)

for i in range(0,100,5):  # third number here is saying count by 5's
    print("i is {}".format(i))

for i in range(1,13):  # will go 1 - 12
    for j in range(1,13):
        print("{1} times {0} is {2}".format(i, j, i * j))
    print("++++++++++++++++++++++++++++++++++")