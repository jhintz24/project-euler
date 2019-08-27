#
# Copyright (c) Justin Hintz, 2019. All rights reserved.
# Project Euler - Problem 002
#
# Python 3.7.4
#

import time

# Straightforward and simple.
def fibonacci(n):

    returnSum = 0
    n0 = 0
    n1 = 1

    for x in range(1, n):
        nNext = n0 + n1
        if nNext > n:
            break
        if nNext % 2 == 0:
            returnSum = returnSum + nNext
        n0 = n1
        n1 = nNext

    return returnSum


startTime = time.time()
print('Answer: ', fibonacci(4000000))
endTime = time.time()
print('Time: ', endTime - startTime)