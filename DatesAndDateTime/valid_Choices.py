# this is my set to see if a user picked a valid choice.  if their choice isn't in this set, they
# must choose again
valid_choice = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
print(valid_choice)
user_choice = ''


while user_choice != '0':
    user_choice = input("What is your choice? ")
    if user_choice in valid_choice:
        print("good choice!")
    elif user_choice == '0':
        print("Sorry you want to quit!")
        break

    else:
        print("you're bad at this")