# name = input("Please enter your name ")
# age = int(input("How old are you {0}? ".format(name)))
# print(age)
#
# if age >= 18:  # if it's true, it'll print 'you are old enough to vote.'
#     print("You are old enough to vote.")
#     print("Please put an X in the box.")
# else:  # if it's false, it'll go to the 'else' statement.  if/then/else
#     print("You can't vote.  You need to wait {0} years".format(18 - age))

# print("Please guess a number between 1 and 10: ")
# guess = int(input())
#
# if guess < 5:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == 5:  # double = if you're testing for equality. for not equal !=
#         print("You got it!")
#     else:
#         print("You're bad at this.")
# elif guess > 5:
#     print("Please guess lower.")
#     guess = int(input())
#     if guess == 5:
#         print("You got it!")
#     else:
#         print("You're bad at this.")
# else:
#     print("You got it on the first try.")

# a more efficient way would be
# print("Please guess a number between 1 and 10: ")
# guess = int(input())
#
# if guess != 5:
#     if guess < 5:
#         print("Please guess higher.")
#     else:  # guess must be greater than 5
#         print("Please guess lower")
#     guess = int(input())  # if both of the above aren't true then guess again
#     if guess == 5:
#         print("You got it!")
#     else:
#         print("You're bad at this.")
# else:
#     print("You got it on the first try.")
#
# age = int(input("How old are you? "))

# if (age >= 16) and (age <= 65):  # parenthesis aren't necessary, but make it easier to read
#     print("have a good day at work.")
#
# age = int(input("How old are you? "))
# if 16 <= age <= 65:
#     print("have a good day at work")

# if (age < 16) or (age > 65):  # one of these has to be true
#     print("enjoy your free time")
# else:  # if neither was true
#     print("have a great day at work")

# x = "false"
#
# if x:
#     print("x is true")
#
# x = input("please enter some text: ")
#
# if x:
#     print("You entered '{}'".format(x))
# else:
#     print("you are bad at this")

# print(not False)
# print(not True)
#
# age = int(input("How old are you? "))
# if not(age < 18):
#     print("""You're old enough to vote.
#     Please put an X in the box. """)
# else:
#     print("You're not old enough to vote. Please come back in {0} years. ".format(18 - age))

parrot = "Norwegian Blue"

letter = input("Enter a character: ")

if letter in parrot:  # note that the evaluation is case sensitive
    print("give me a letter {}!".format(letter))
else:
    print("You're bad at this!")

# You could also do 'not in'
letter = input("What's your letter, joker?  ")
if letter not in parrot:
    print("You're bad at this!")
else:
    print("Very good.  You guessed the letter {0}!".format(letter))
