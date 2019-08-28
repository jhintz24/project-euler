#
# Copyright (c) Justin Hintz, 2019. All rights reserved.
# Project Euler - Problem 037
#
# Python 3.7.4
#

import time
import EulerLib as lib

def ansFunction():

    primes = [2]
    truncatablePrimes = []
    x = 3

    while True:
        if lib.isPrime(x):
            primes.append(x)

            if isTruncatable(x, primes):
                print(x)
                truncatablePrimes.append(x)
                if len(truncatablePrimes) == 11:
                    break
        x += 2

    return sum(truncatablePrimes)

def isTruncatable(n, primes):

    n = str(n)
    if len(n) == 1:
        return False

    # Check left
    left = n
    while len(left) > 1:
        left = left[1:]
        if int(left) not in primes:
            return False

    # Check right
    right = n
    while len(right) > 1:
        right = right[:-1]
        if int(right) not in primes:
            return False

    return True


startTime = time.time()
print('Answer: ', ansFunction())
endTime = time.time()
print ('Time: ', endTime - startTime)