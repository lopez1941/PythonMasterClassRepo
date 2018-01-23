#  create a generator to return an infinite sequence of odd numbers starting at 1
#  print the first 100 numbers


def oddNumbers():
    oddNum = 1

    while True:
        yield oddNum
        oddNum += 2

def pi_series():
    odds = oddNumbers()
    approximation = 0

    while True:
        approximation += (4 / next(odds))
        yield approximation
        approximation -= (4 / next(odds))
        yield approximation



# odds = fibChallenge()
#
# for i in range(100):
#     print(next(odds))

approx_pi = pi_series()

for x in range(10000000):
    print(next(approx_pi))

