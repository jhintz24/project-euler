#
# Copyright (c) Justin Hintz, 2019. All rights reserved.
# Project Euler - Problem 034
#
# Python 3.7.4
#

import time
import math

def ansFunction():

    returnSum = 0
    for number in range(10,200000): #Semi-arbitrary limit based on analysis. Need to come back to it.
        sum = 0
        for digit in str(number):
            sum += math.factorial(int(digit))

        if sum == number:
            returnSum += number

    return returnSum


startTime = time.time()
print('Answer: ', ansFunction())
endTime = time.time()
print ('Time: ', endTime - startTime)