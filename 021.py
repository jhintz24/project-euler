import math

# Modified function from problem 12
def getDivisors(n):
    x = 1
    divisors = []
    while x < math.sqrt(n):
        if n % x == 0:
            if x not in divisors:
                divisors.append(x)
            if n/x not in divisors and n/x != n: # We do not include n for some reason
                divisors.append(n/x)
        x = x + 1
    return divisors

def ansFunction(n):
    amicableNumbers = []

    for a in range(1,n):
        if a not in amicableNumbers:
            aDivisors = getDivisors(a)
            b = sum(aDivisors)
            bDivisors = getDivisors(b)

            if a == sum(bDivisors) and a != b and b < n:
                amicableNumbers.append(a)
                amicableNumbers.append(b)

    return sum(amicableNumbers)

print ansFunction(10000)
