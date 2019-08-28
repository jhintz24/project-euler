#
# Copyright (c) Justin Hintz, 2019. All rights reserved.
# Project Euler - Problem 057
#
# Python 3.7.4
#

import time
import math

def ansFunction(n):

    num = 3
    denom = 2
    count = 0

    for x in range(n):
        if int(math.log(num, 10)) > int(math.log(denom, 10)):
            count += 1
        denom, num = num + denom, num + (2 * denom)

    return count


startTime = time.time()
print('Answer: ', ansFunction(1001))
endTime = time.time()
print ('Time: ', endTime - startTime)