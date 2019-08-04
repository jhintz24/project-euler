
def isPandigital(n):
    strN = str(n)
    if len(strN) != 9:
        return False

    for x in range(1, 10):
        if strN.find(str(x)) < 0:
            return False
    else:
        return True


def ansFunction():
    pandigitals = {}
    for a in range(1,5000): #5,000 is slightly arbitrary. Need proof
        for b in range(1,5000):
            product = a * b
            combo = str(product) + str(a) + str(b)
            if isPandigital(combo):
                pandigitals[product] = 1

    return sum(pandigitals.keys())

print ansFunction()
