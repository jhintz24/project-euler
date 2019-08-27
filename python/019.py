#
# Copyright (c) Justin Hintz, 2019. All rights reserved.
# Project Euler - Problem 019
#
# Python 3.7.4
#

import time

# Could use some refactoring
def isLeapYear(year):

    if year % 100 == 0 and year % 400 == 0:
        return True
    if year % 4 == 0:
        return True
    return False

def ansFunction():

    day = 365
    month = 12
    monthDayCount = 31
    year = 1899
    sundayCount = 0

    while year < 2001:

        day = day + 7
        monthDayCount = monthDayCount + 7

        if not isLeapYear(year) and day > 365:
            day = day - 365
            year = year + 1
            month = 1
            monthDayCount = day

        if isLeapYear(year) and day > 366:
            day = day - 366
            year = year + 1
            month = 1
            monthDayCount = day

        if month in (4, 6, 9, 11) and monthDayCount > 30:
            monthDayCount = monthDayCount - 30
            month = month + 1

        if month in (1, 3, 5, 7, 8, 10, 12) and monthDayCount > 31:
            monthDayCount = monthDayCount - 31
            month = month + 1

        if month == 2 and not isLeapYear(year) and monthDayCount > 28:
            monthDayCount = monthDayCount - 28
            month  = month + 1

        if month == 2 and isLeapYear(year) and monthDayCount > 29:
            monthDayCount = monthDayCount - 29
            month = month + 1

        if year > 1900 and monthDayCount == 1:
            sundayCount = sundayCount + 1

        #print(day, month, monthDayCount, year)


    return sundayCount


startTime = time.time()
print('Answer: ', ansFunction())
endTime = time.time()
print ('Time: ', endTime - startTime)