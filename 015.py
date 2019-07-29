import math

#Simple n choose k problem
def ansFunction(n,k):
    return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))

print ansFunction(40,20)