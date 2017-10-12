user_input = input("Please type in two integer numbers separated by a comma: ")
input_split = user_input.split(',')

try:
    num1, num2 = input_split
    print(int(num1) // int(num2))
except (ValueError, TypeError, ZeroDivisionError):
    print("Well, that didn't work")




