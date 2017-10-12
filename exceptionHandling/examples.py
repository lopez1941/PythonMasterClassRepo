def factorial(n):
    # n! can also be defined as n* (n - 1)!

    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

try:
    print(factorial(900))
# you can combine except clauses
except (RecursionError, ZeroDivisionError):
    print("This program can't calculate factorials that large")


print("Program Terminating!")
