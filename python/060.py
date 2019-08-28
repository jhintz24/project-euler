#
# Copyright (c) Justin Hintz, 2019. All rights reserved.
# Project Euler - Problem 060
#
# Python 3.7.4
#

import time
import EulerLib as lib

def ansFunction():

    # Calculate all primes up to 10,000 (arbitrary)
    # Exclude 2 and 5 because a prime number cannot end with 2 or 5
    primes = [3]
    for x in range(7, 10000, 2):
        if lib.isPrime(x):
            primes.append(x)


    for i in range(len(primes)):
        a = [primes[i]]
        #print('a: ', a)
        for j in range(i + 1, len(primes)):
            b = list(a)
            #print('b: ', b)
            b.append(primes[j])
            if not isConcatable(b):
                continue
            for k in range(j +1, len(primes)):
                c = list(b)
                #print('c: ', c)
                c.append(primes[k])
                if not isConcatable(c):
                    continue
                for l in range(k + 1, len(primes)):
                    d = list(c)
                    #print('d: ', d)
                    d.append(primes[l])
                    if not isConcatable(d):
                        continue
                    for m in range(l + 1, len(primes)):
                        e = list(d)
                        #print('e: ', e)
                        e.append(primes[m])
                        if isConcatable(e):
                            return sum(e)
                        else:
                            continue

def isConcatable(numbers):

    for x in range(len(numbers)):
        for y in range(x + 1, len(numbers)):
            if not lib.isPrime(int(str(numbers[x]) + str(numbers[y]))) or not lib.isPrime(int(str(numbers[y]) + str(numbers[x]))):
                return False

    return True



startTime = time.time()
print('Answer: ', ansFunction())
endTime = time.time()
print('Time: ', endTime - startTime)