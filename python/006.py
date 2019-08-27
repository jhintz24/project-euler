#
# Copyright (c) Justin Hintz, 2019. All rights reserved.
# Project Euler - Problem 006
#
# Python 3.7.4
#

import time

# This can be sped up slightly by recognizing that (1+2..+99,100) = (50*101)
def ansFunction(n):

    sum1 = 0
    sum2 = 0
    for x in range(1,n + 1):
        sum1 = sum1 + (x**2)
        sum2 = sum2 + x

    sum2 = sum2**2

    return sum2 - sum1


startTime = time.time()
print('Answer: ', ansFunction(100))
endTime = time.time()
print('Time: ', endTime - startTime)