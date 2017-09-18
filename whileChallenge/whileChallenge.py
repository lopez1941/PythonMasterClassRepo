import random

highest = 10
lowest = 1
guess = 0
answer = random.randint(lowest, highest)

print("Guess a number between {0} and {1}. Press 0 to quit: ".format(lowest, highest))
guess = int(input())

while guess != 0:
    if guess == answer:
        print("You got it! The number was {0}!".format(answer))
        break
    elif guess < answer:
        print("Too low.  Guess higher: ")
    else:
        print("Too high.  Guess lower: ")
    guess = int(input())
else:
    print("Quitters never win!")


# instructor's answer
# print("Guess a number between {0} and {1}. Press 0 to quit: ".format(lowest, highest))
# guess = 0
# while guess != answer:
#     guess = int(input())
#     if guess == 0:
#         break
#     if guess < answer:
#         print("Please guess higher: ")
#     elif guess > answer:
#         print("Please guess lower: ")
#     else:
#         print("well done you guessed it")
