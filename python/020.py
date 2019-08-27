#
# Copyright (c) Justin Hintz, 2019. All rights reserved.
# Project Euler - Problem 020
#
# Python 3.7.4
#

import time
import math

# Trivial for computer
def ansFunction(n):

    num = str(math.factorial(n))
    sum = 0
    for digit in num:
        sum = sum + int(digit)

    return sum


startTime = time.time()
print('Answer: ', ansFunction(100))
endTime = time.time()
print ('Time: ', endTime - startTime)
