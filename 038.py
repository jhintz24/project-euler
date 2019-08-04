#Reuse from problem 032
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
    largestPandigital = 0

    for i in range(1,10000): #Semi-arbitrary boundary
        x = 1
        pandigital = ''
        while True:
            pandigital += str(i*x)

            if len(pandigital) > 9:
                break

            if isPandigital(pandigital) and int(pandigital) > largestPandigital:
                largestPandigital = int(pandigital)
            x += 1

    return largestPandigital

print ansFunction()