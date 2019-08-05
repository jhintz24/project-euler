import math

#We can use the core (brute-force) logic from problem 037.
def isPrime(n):

    if n <= 1: #Modification in problem 037
        return False

    if n % 2 == 0: #Modification from problem 027
        return False

    # Only search until the sqrt of the current number, increasing by two (only odd numbers)
    for x in range(3, int(math.sqrt(n)) + 1, 2):
        if n % x == 0:
            return False

    return True

def ansFunction():

    x = 3
    primes = [2]
    while True:
        if isPrime(x):
            primes.append(x)
        else:
            flag = 0
            for prime in primes:
                y = 1
                calculation = 0
                while calculation < x:
                    calculation = prime + (2 * (y**2))
                    if calculation == x:
                        flag = 1
                        break
                    y += 1
                if flag == 1:
                    break
            if flag == 0:
                return x
        x += 2

print ansFunction()