#
# Copyright (c) Justin Hintz, 2019. All rights reserved.
# Project Euler - Problem 036
#
# Python 3.7.4
#

import time
import EulerLib as lib

def ansFunction(n):

    palindromes = []
    for x in range(n):
        if lib.isPalindrome(x):
            base2 = bin(x)[2:]
            if lib.isPalindrome(base2):
                palindromes.append(x)

    return sum(palindromes)


startTime = time.time()
print('Answer: ', ansFunction(1000000))
endTime = time.time()
print ('Time: ', endTime - startTime)