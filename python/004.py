#
# Copyright (c) Justin Hintz, 2019. All rights reserved.
# Project Euler - Problem 004
#
# Python 3.7.4
#

import time
import EulerLib as lib

# Brute force is fast for only 3 digits
def largestPalindrome():

    n1 = 999
    largest = 0
    for x in range(n1, 99, -1):
        for y in range(x, 99, -1):
            z = x * y
            if lib.isPalindrome(z):
                if z > largest:
                    largest = z

    return largest


startTime = time.time()
print('Answer: ', largestPalindrome())
endTime = time.time()
print('Time: ', endTime - startTime)


