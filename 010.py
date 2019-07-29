import math

#We can use the core (brute-force) logic from problem 007.
def isPrime(n):

    # Only search until the sqrt of the current number, increasing by two (only odd numbers)
    for x in range(3, int(math.sqrt(n)) + 1, 2):
        if n % x == 0:
            return False

    return True

def ansFunction(n):
    if n <= 2:
        return 0

    ans = 2
    for x in range(3,n,2):
        if isPrime(x):
            ans = ans + x

    return ans

print ansFunction(2000000)
