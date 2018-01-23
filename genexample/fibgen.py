def fibonacci():
    current, previous = 0,1

    while True:
        current, previous = current + previous, current
        yield current

fib = fibonacci()

for i in range(0,21):
    print(next(fib))
