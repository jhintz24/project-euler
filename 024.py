import math

def ansFunction(n):
    digits = [0,1,2,3,4,5,6,7,8,9]
    permutation = ''
    numberOfDigits = len(digits)
    while len(permutation) < numberOfDigits:
        fac = math.factorial(len(digits))
        segment = fac / len(digits)
        index = n/segment
        permutation += str(digits[index])
        digits.pop(index)
        n = n % segment
    return permutation

print ansFunction(999999)