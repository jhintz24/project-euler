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

#Take the core logic from problem 028
# Takes a few minutes...
def ansFunction():

    primes = []
    nonPrimes = [1]
    currentDimension = 2
    sideSize = 3
    count = 1
    x = 2
    while True:

        if x > sideSize ** 2:
            if len(primes) > 0 and len(nonPrimes) > 0:
                ratio = float(len(primes)) / float(len(primes) + len(nonPrimes))
                print x, sideSize, ratio
                if ratio < .1:
                    return sideSize

            sideSize += 2
            currentDimension += 2

        if count == currentDimension:
            if isPrime(x):
                primes.append(x)
            else:
                nonPrimes.append(x)

            count = 1
        else:
            count += 1

        x += 1


print ansFunction()