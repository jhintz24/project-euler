#
# Copyright (c) Justin Hintz, 2019. All rights reserved.
# Project Euler - Problem 010
#
# Python 3.7.4
#

import time
import EulerLib as lib

def ansFunction(n):

    ans = 2
    for x in range(3,n,2):
        if lib.isPrime(x):
            ans = ans + x

    return ans

startTime = time.time()
print('Answer: ', ansFunction(2000000))
endTime = time.time()
print ('Time: ', endTime - startTime)
