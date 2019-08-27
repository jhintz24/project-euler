#
# Copyright (c) Justin Hintz, 2019. All rights reserved.
# Project Euler - Problem 033
#
# Python 3.7.4
#

import time
import math

#Not exactly sure how this one is solved - need to come back to it
def ansFunction():

    num = 1
    denom = 1
    for d in range(10, 100):
        for n in range(10, d):
            n0 = n % 10
            n1 = n // 10
            d0 = d % 10
            d1 = d // 10
            if (n1 == d0 and n0 * d == n * d1) or (n0 == d1 and n1 * d == n * d0):
                num *= n
                denom *= d

    return str(denom // math.gcd(num, denom))


startTime = time.time()
print('Answer: ', ansFunction())
endTime = time.time()
print ('Time: ', endTime - startTime)