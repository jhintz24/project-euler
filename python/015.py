#
# Copyright (c) Justin Hintz, 2019. All rights reserved.
# Project Euler - Problem 015
#
# Python 3.7.4
#

import time
import math

# Simple n choose k problem
def ansFunction(n, k):

    return math.factorial(n) // (math.factorial(k)*math.factorial(n-k))


startTime = time.time()
print('Answer: ', ansFunction(40, 20))
endTime = time.time()
print ('Time: ', endTime - startTime)