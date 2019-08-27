#
# Copyright (c) Justin Hintz, 2019. All rights reserved.
# Project Euler - Problem 016
#
# Python 3.7.4
#

import time

def ansFunction(n):

    num = str(2 ** n)
    ans = 0
    for digit in num:
        ans = ans + int(digit)

    return ans


startTime = time.time()
print('Answer: ', ansFunction(1000))
endTime = time.time()
print ('Time: ', endTime - startTime)