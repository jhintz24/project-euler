#
# Copyright (c) Justin Hintz, 2019. All rights reserved.
# Project Euler - Problem 040
#
# Python 3.7.4
#

import time

def ansFunction():
    d = ''
    x = 1
    while True:
        d += str(x)
        if len(d) >= 1000000:
            break
        x += 1

    return int(d[0]) * int(d[9]) * int(d[99]) * int(d[999]) * int(d[9999]) * int(d[99999]) * int(d[999999])


startTime = time.time()
print('Answer: ', ansFunction())
endTime = time.time()
print ('Time: ', endTime - startTime)