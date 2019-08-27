#
# Copyright (c) Justin Hintz, 2019. All rights reserved.
# Project Euler - Problem 057
#
# Python 3.7.4
#

import time

#Need to work on this
def ansFunction(n):

    count = 0
    num = 0
    denom = 1
    for x in range(n):
        num, denom = denom, denom * 2 + num
        if len(str(num + denom)) > len(str(denom)):
            count += 1
    return count


startTime = time.time()
print('Answer: ', ansFunction(1000))
endTime = time.time()
print ('Time: ', endTime - startTime)