#
# Copyright (c) Justin Hintz, 2019. All rights reserved.
# Project Euler - Problem 049
#
# Python 3.7.4
#

import time
import EulerLib as lib

def containSameDigits(x, y , z):
    return sorted(str(x)) == sorted(str(y)) == sorted(str(z))

def ansFunction():
    x = 1
    while True:
        x1 = 1000
        x2 = x1 + x
        x3 = x2 + x
        while x3 < 10000:
            if lib.isPrime(x1) and lib.isPrime(x2) and lib.isPrime(x3) and containSameDigits(x1, x2, x3):
                if x1 != 1487 and x2 != 4817:
                    return str(x1) + str(x2) + str(x3)
            x1 += 1
            x2 = x1 + x
            x3 = x2 + x

        x += 1


startTime = time.time()
print('Answer: ', ansFunction())
endTime = time.time()
print ('Time: ', endTime - startTime)
