#
# Copyright (c) Justin Hintz, 2019. All rights reserved.
# Project Euler - Problem 023
#
# Python 3.7.4
#

import time
import EulerLib as lib

def ansFunction():

    abundantNumbers = []
    for x in range(1,28124): # There is a clever way to do this
        divisors = lib.getDivisors(x)
        if sum(divisors) > x:
            abundantNumbers.append(x)

    ans = [0] * 28124
    for x in range(len(abundantNumbers)):
        for y in range(x, len(abundantNumbers)):
            if abundantNumbers[x] + abundantNumbers[y] < 28124:
                ans[abundantNumbers[x] + abundantNumbers[y]] = 1
            else:
                break

    count = 0
    for x, y in enumerate(ans):
        if y == 0:
            count += x

    return count


startTime = time.time()
print('Answer: ', ansFunction())
endTime = time.time()
print ('Time: ', endTime - startTime)
