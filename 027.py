import math

#We can use the core (brute-force) logic from problem 007.
def isPrime(n):

    if n < 0: #Modification from problem 007
        return False

    # Only search until the sqrt of the current number, increasing by two (only odd numbers)
    for x in range(3, int(math.sqrt(n)) + 1, 2):
        if n % x == 0:
            return False

    return True

def getConsecutiveN(a, b):
    n = 0
    while True:
        result = (n ** 2) + (a * n) + b
        if isPrime(result):
            n += 1
        else:
            break
    return n


def ansFunction():
    aLimit = 1000
    bLimit = 1001

    #b must be prime
    bPrimes = []
    for x in range (2,bLimit):
        if isPrime(x):
            bPrimes.append(x)

    largestN = 0
    bestA = 0
    bestB = 0

    for a in range(-(aLimit-1),aLimit,2): #a must be odd
        for b in bPrimes:
            n1 = getConsecutiveN(a, b)
            n2 = getConsecutiveN(a, -b)

            if n1 > largestN:
                largestN = n1
                bestA = a
                bestB = b
            if n2 > largestN:
                largestN = n2
                bestA = a
                bestB = -b

    return bestA * bestB

print ansFunction()





