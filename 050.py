import math

#We can use the core (brute-force) logic from problem 049.
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

def ansFunction():

    primes = [2]
    longestChain = 0
    longestChainPrime = 0
    for x in range(3,1000000, 2):
        print x
        if isPrime(x):
            for z in range(len(primes)):
                y = z
                sum = 0
                count = 0
                while y < len(primes):
                    sum += primes[y]
                    count += 1
                    if sum == x and count > longestChain:
                        longestChain = count
                        longestChainPrime = x
                        break
                    if sum > x:
                        break
                    y += 1
            primes.append(x)

    return longestChainPrime


print ansFunction()
