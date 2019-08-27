#
# Copyright (c) Justin Hintz, 2019. All rights reserved.
# Project Euler - Problem 021
#
# Python 3.7.4
#

import time
import EulerLib as lib

def ansFunction(n):
    amicableNumbers = []

    for a in range(1,n):
        if a not in amicableNumbers:
            aDivisors = lib.getDivisors(a)
            b = sum(aDivisors)
            bDivisors = lib.getDivisors(b)

            if a == sum(bDivisors) and a != b and b < n:
                amicableNumbers.append(a)
                amicableNumbers.append(b)

    return sum(amicableNumbers)


startTime = time.time()
print('Answer: ', ansFunction(10000))
endTime = time.time()
print ('Time: ', endTime - startTime)
