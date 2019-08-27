#
# Copyright (c) Justin Hintz, 2019. All rights reserved.
# Project Euler - Problem 005
#
# Python 3.7.4
#

import time
import EulerLib as lib

def smallestNumber():

    ans = 1
    for x in range(2,21):
        if ans % x != 0:
            ans = ans * lib.largestPrime(x)

    return ans


startTime = time.time()
print('Answer: ', smallestNumber())
endTime = time.time()
print('Time: ', endTime - startTime)