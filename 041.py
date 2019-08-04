import itertools
import math

#We can use the core (brute-force) logic from problem 035.
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

    digits = '123456789'
    largestPrime = 0
    for x in range(len(digits)):
        for combo in itertools.permutations(digits,len(digits)):
            number = ''
            for digit in combo:
                number += digit
            number = int(number)
            if isPrime(number) and number > largestPrime:
                largestPrime = number
        if largestPrime > 0:
            return largestPrime
        digits = digits[:-1]


print ansFunction()