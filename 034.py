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


print ansFunction()