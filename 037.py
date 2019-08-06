import math
import itertools

#isPrime function wasn't working for 2!!! Need to fix in other solutions. So stupid...
#We can use the core (brute-force) logic from problem 035.
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
    ans = sum(itertools.islice(itertools.ifilter(is_truncatable_prime, itertools.count(10)), 11))
    return ans


def is_truncatable_prime(n):
    # Test if left-truncatable
    i = 10
    while i <= n:
        if not isPrime(n % i):
            return False
        i *= 10

    # Test if right-truncatable
    while n > 0:
        if not isPrime(n):
            return False
        n //= 10

    return True

print ansFunction()