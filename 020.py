import math

# Trivial for computer
def ansFunction(n):
    num = str(math.factorial(n))
    sum = 0
    for digit in num:
        sum = sum + int(digit)

    return sum

print ansFunction(100)
