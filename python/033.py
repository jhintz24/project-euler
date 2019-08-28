#
# Copyright (c) Justin Hintz, 2019. All rights reserved.
# Project Euler - Problem 033
#
# Python 3.7.4
#

import time
import fractions

def ansFunction():

    ans = fractions.Fraction(1, 1)
    for a in range(1, 10):
        for b in range(1, 10):
            for c in range(1, 10):
                num = int(str(a) + str(b))
                denom = int(str(b) + str(c))
                frac1 = fractions.Fraction(num, denom)
                frac2 = fractions.Fraction(a, c)

                if num < denom and frac1 == frac2:
                    ans *= frac1
    return ans


startTime = time.time()
print('Answer: ', ansFunction())
endTime = time.time()
print ('Time: ', endTime - startTime)