import sys

def get_user_input():
    while True:
        try:
            input_received = int(input("Please enter an integer number: "))
            return input_received
        except ValueError:
            print("Oops, try again.  That wasn't a valid integer!")
        except EOFError:
            sys.exit(1)
        finally:
            print("The finally clause always executes")


number1 = get_user_input()
number2 = get_user_input()

try:
    print("The first number divided by the second number is {}".format(number1 / number2))
except ZeroDivisionError:
    print("Whoa, there.  You can't divide by zero, dude!")
    sys.exit(2)
else:  # else is only executed if the try completes, finally will execute regardless
    print("Division performed successfully!")

