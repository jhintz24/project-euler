#
# Copyright (c) Justin Hintz, 2019. All rights reserved.
# Project Euler - Problem 053
#
# Python 3.7.4
#

import time
import math

# Could make faster by cutting r for loop
def ansFunction():

    count = 0
    for n in range(1, 101):
        for r in range(n+1):
            if math.factorial(n) / (math.factorial(r) * (math.factorial(n-r))) > 1000000:
                count += 1

    return count


startTime = time.time()
print('Answer: ', ansFunction())
endTime = time.time()
print ('Time: ', endTime - startTime)