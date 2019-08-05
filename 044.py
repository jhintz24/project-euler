
#This gets the right answer but the logic is not exactly correct
def ansFunction():
    pentagonalNumbers = []
    n = 1
    while True:
        next = n * ((3 * n) - 1) / 2
        pentagonalNumbers.append(next)
        for i in range(len(pentagonalNumbers)-1):
            j = pentagonalNumbers[i]
            k = next - j
            #print "k, j", k, j
            if k in pentagonalNumbers:
                diff = abs(k - j)
                if diff in pentagonalNumbers:
                    return diff
        n += 1

print ansFunction()
