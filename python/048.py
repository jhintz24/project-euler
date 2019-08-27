#
# Copyright (c) Justin Hintz, 2019. All rights reserved.
# Project Euler - Problem 048
#
# Python 3.7.4
#

import time

def ansFunction(n):

    sum = 0
    for x in range(1, n):
        sum += (x ** x)

    return str(sum)[-10:]


startTime = time.time()
print('Answer: ', ansFunction(1001))
endTime = time.time()
print ('Time: ', endTime - startTime)