#
# Copyright (c) Justin Hintz, 2019. All rights reserved.
# Project Euler - Problem 037
#
# Python 3.7.4
#

import time
import itertools
import EulerLib as lib

def ansFunction():
    ans = sum(itertools.islice(itertools.ifilter(isTruncatablePrime, itertools.count(10)), 11))
    return ans

def isTruncatablePrime(n):
    # Test if left-truncatable
    i = 10
    while i <= n:
        if not lib.isPrime(n % i):
            return False
        i *= 10

    # Test if right-truncatable
    while n > 0:
        if not lib.isPrime(n):
            return False
        n //= 10

    return True


startTime = time.time()
print('Answer: ', ansFunction())
endTime = time.time()
print ('Time: ', endTime - startTime)