#
# Copyright (c) Justin Hintz, 2019. All rights reserved.
# Project Euler - Problem 039
#
# Python 3.7.4
#

import time

# Use the core logic from problem 009
def ansFunction(n):

    maxSolutions = 0
    maxP = 0
    for p in range(3,n):
        pCount = 0

        for a in range(1,p-1):
            for b in range(a+1,p):
                c = p - a - b
                if a ** 2 + b ** 2 == c ** 2:
                    pCount += 1

        if pCount > maxSolutions:
            maxSolutions = pCount
            maxP = p

    return maxP


startTime = time.time()
print('Answer: ', ansFunction(1001))
endTime = time.time()
print ('Time: ', endTime - startTime)