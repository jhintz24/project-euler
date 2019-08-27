#
# Copyright (c) Justin Hintz, 2019. All rights reserved.
# Project Euler - Problem 030
#
# Python 3.7.4
#

import time

def ansFunction():

    sum = 0
    for x in range(2,1000000): # 1,000,000 is arbitrary is gives the right answer. Need to find pattern.
        digitSum = 0
        for char in str(x):
            digitSum += int(char)**5

        if x == digitSum:
            sum += x

    return sum


startTime = time.time()
print('Answer: ', ansFunction())
endTime = time.time()
print ('Time: ', endTime - startTime)