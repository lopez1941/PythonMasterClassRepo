#  while loops are used to execute code as long as a condition is true

# for i in range(10):
#     print("i is now {0}".format(i))
#
# i = 0  # have to give i a value when using a while loop, it has to have
#        # an initial value
# while i < 10:
#     print("i is now {0}".format(i))
#     i += 1

# available_exits = ["east", "north", "east", "south"]
# chosen_exit = ''
#
# while chosen_exit not in available_exits:
#     chosen_exit = input("choose a direction: ")
#     if chosen_exit == "quit":
#         print("Game over")
#         break  # breaks out of the while loop, including the else statement below
# else:
#     print("you moved!")

import random

highest = 10
answer = random.randint(1, highest)

print("Please guess a number between 1 and {0}: ".format(highest))
guess = int(input())

if guess != answer:
    if guess < answer:
        print("Guess higher")
    else:
        print("guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done, mind reader!")
    else:
        print("you're bad at this")
else:
    print("well done, mind reader!")
