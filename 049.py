import math

#We can use the core (brute-force) logic from problem 046.
def isPrime(n):

    if n <= 1: #Modification in problem 037
        return False

    if n == 2: #Modification in problem 037
        return True

    if n % 2 == 0: #Modification from problem 027
        return False

    # Only search until the sqrt of the current number, increasing by two (only odd numbers)
    for x in range(3, int(math.sqrt(n)) + 1, 2):
        if n % x == 0:
            return False

    return True

def containSameDigits(x, y , z):
    return sorted(str(x)) == sorted(str(y)) == sorted(str(z))

def ansFunction():
    x = 1
    while True:
        x1 = 1000
        x2 = x1 + x
        x3 = x2 + x
        while x3 < 10000:
            if isPrime(x1) and isPrime(x2) and isPrime(x3) and containSameDigits(x1, x2, x3):
                if x1 != 1487 and x2 != 4817:
                    return str(x1) + str(x2) + str(x3)
            x1 += 1
            x2 = x1 + x
            x3 = x2 + x

        x += 1

print ansFunction()
