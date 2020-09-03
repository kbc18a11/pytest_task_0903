import math as m


def calcDistance(ax, ay, bx, by):
    return m.sqrt((bx - ax) ** 2 + (bx - ay) ** 2)


def isPrime(x):
    primeNumbers = [2, 3, 5, 7]

    if x == 1 | x == 0 | x < 0:
        return False

    if x in primeNumbers:
        return True

    for primeNumber in primeNumbers:
        if x % primeNumber == 1:
            return True

    return False


print(isPrime(-7))
