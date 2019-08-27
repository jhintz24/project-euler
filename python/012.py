#
# Copyright (c) Justin Hintz, 2019. All rights reserved.
# Project Euler - Problem 012
#
# Python 3.7.4
#

import time
import EulerLib as lib

def ansFunction(n):

    x = 1
    y = 1
    while True:
        z = lib.getNumberOfDivisors(y)
        if z > n:
            return y
        x = x + 1
        y = y + x


startTime = time.time()
print('Answer: ', ansFunction(500))
endTime = time.time()
print ('Time: ', endTime - startTime)