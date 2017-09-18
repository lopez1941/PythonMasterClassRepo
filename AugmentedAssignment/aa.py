# using += instead of bob = bob + something
# bob += something

number = "9,223,372,036,854,775,807"
cleanedNumber = ''

for i in range(0, len(number)):
    if number[i] in '0123456789':
        #  cleanedNumber = cleanedNumber + number[i], old way of doing it
        cleanedNumber += number[i]  # augmented assignment only evaluates cleaned number once
        # this is a cleaner more efficient way to do it
newNumber = int(cleanedNumber)
print("The number is {}".format(newNumber))

x = 23
x += 1
print(x)

x -= 4 # 24 - 4
print(x)

x *= 5 # 20 * 5
print(x)

x /= 4
print(x)

x **= 2
print(x)

x %= 60
print(x)

greeting = "good "
greeting += "morning "
print(greeting)
greeting *= 5
print(greeting)

# +=, -=, /=, %=, **=, <<=, >>=, &=, |=