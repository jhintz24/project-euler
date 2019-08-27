#
# Copyright (c) Justin Hintz, 2019. All rights reserved.
# A simple utilities library for solving Project Euler problems
#
# Python 3.7.4
#

import math

# Determines whether a given number is prime
def isPrime(n):

    if n <= 1:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    # Only search until the sqrt of the current number, increasing by two (only odd numbers)
    for x in range(3, int(math.sqrt(n)) + 1, 2):
        if n % x == 0:
            return False

    return True

# Determines the largest prime factor for a given number
def largestPrime(n):

    x = 2
    while n > x:
        if n % x == 0:
            n = n // x
        else:
            x = x + 1
    return x

# Returns prime factors of a given number
def getPrimeFactors(n):

    primeFactors = []
    x = 2
    while n >= x:
        if n % x == 0:
            for factor in primeFactors:
                if factor[0] == x:
                    factor[1] += 1
                    break
            else:
                primeFactors.append([x, 1])
            n = n / x
        else:
            x = x + 1

    return primeFactors

# Determines whether a given input is a palindrome
def isPalindrome(n):

    n = str(n)

    if n == n[::-1]:
        return True
    else:
        return False

# Returns the number of divisors for a given number
def getNumberOfDivisors(n):

    x = 1
    count = 0
    while x < math.sqrt(n):
        if n % x == 0:
            if n // x == x:
                count = count + 1
            else:
                count = count + 2
        x = x + 1
    return count

# Returns divisors for a given number
def getDivisors(n):

    x = 1
    divisors = []
    while x <= math.sqrt(n):
        if n % x == 0:
            if x not in divisors:
                divisors.append(x)
            if n // x not in divisors and n // x != n: # We do not include n
                divisors.append(n // x)
        x = x + 1

    return divisors

# Determines whether a given number is pandigital
def isPandigital(n):

    strN = str(n)
    if len(strN) != 9:
        return False

    for x in range(1, 10):
        if strN.find(str(x)) < 0:
            return False
    else:
        return True

# Returns the INT value of a string
def getWordIntValue(word):
    offset = 64 # ASCII value of 'A' is 65
    sum = 0
    for char in word:
        sum = sum + (ord(char)-offset)
    return sum