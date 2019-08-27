#
# Copyright (c) Justin Hintz, 2019. All rights reserved.
# Project Euler - Problem 003
#
# Python 3.7.4
#

import time

# Simple and straightforward.
def largestPrime(n):

    x = 2
    while n > x:
        if n % x == 0:
            n = n // x
        else:
            x = x + 1

    return x


startTime = time.time()
print('Answer: ', largestPrime(600851475143))
endTime = time.time()
print('Time: ', endTime - startTime)