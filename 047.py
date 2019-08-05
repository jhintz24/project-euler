#Repurpose largestPrime function from prob 003
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
            n = n/x
        else:
            x = x + 1

    return primeFactors

def areUnique(x1, x2, x3, x4):
    for factor in x1:
        if factor in x2 or factor in x3 or factor in x4:
            return False

    for factor in x2:
        if factor in x3 or factor in x4:
            return False

    for factor in x3:
        if factor in x4:
            return False

    return True

def ansFunction():
    factorDict = {}
    x = 4
    while True:
        x4Factors = getPrimeFactors(x)
        factorDict[x] = x4Factors
        if x - 1 in factorDict:
            x3Factors = factorDict[x - 1]
        if x - 2 in factorDict:
            x2Factors = factorDict[x - 2]
        if x - 3 in factorDict:
            x1Factors = factorDict[x - 3]

        if len(x4Factors) == 4 and len(x3Factors) == 4 and len(x2Factors) == 4 and len(x1Factors) == 4:
            if areUnique(x1Factors, x2Factors, x3Factors, x4Factors):
                return x - 3
        x += 1



print ansFunction()