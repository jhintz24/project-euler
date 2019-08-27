#
# Copyright (c) Justin Hintz, 2019. All rights reserved.
# Project Euler - Problem 001
#
# Python 3.7.4
#

import time

def ansFunction(n):

    # A simple list comprehension works quickly enough
    return sum([x for x in range(n) if (x % 3 == 0 or x % 5 == 0)])


startTime = time.time()
print('Answer: ', ansFunction(1000))
endTime = time.time()
print('Time: ', endTime - startTime)