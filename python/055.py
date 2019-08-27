#
# Copyright (c) Justin Hintz, 2019. All rights reserved.
# Project Euler - Problem 055
#
# Python 3.7.4
#

import time
import EulerLib as lib

def ansFunction(n):

    count = 0
    for x in range(1,n):
        z = x
        for y in range(1, 50):
            z = z + int(str(z)[::-1])
            if lib.isPalindrome(z):
                break
        else:
            count += 1

    return count


startTime = time.time()
print('Answer: ', ansFunction(10000))
endTime = time.time()
print ('Time: ', endTime - startTime)
