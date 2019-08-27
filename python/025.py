#
# Copyright (c) Justin Hintz, 2019. All rights reserved.
# Project Euler - Problem 025
#
# Python 3.7.4
#

import time

def fibonacci(n):

    f1 = 1
    f2 = 1
    index = 2
    fNext = 0
    while len(str(fNext)) < n:
        fNext = f1 + f2
        f1 = f2
        f2 = fNext
        index += 1

    return index


startTime = time.time()
print('Answer: ', fibonacci(1000))
endTime = time.time()
print ('Time: ', endTime - startTime)