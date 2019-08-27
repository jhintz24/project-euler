#
# Copyright (c) Justin Hintz, 2019. All rights reserved.
# Project Euler - Problem 009
#
# Python 3.7.4
#

import time

# Straightforward brute-force search
def ansFunction(n):

    for a in range(1,n-1):
        for b in range(a+1,n):
            c = n - a - b
            if a ** 2 + b ** 2 == c ** 2:
                return a * b * c


startTime = time.time()
print('Answer: ', ansFunction(1000))
endTime = time.time()
print ('Time: ', endTime - startTime)