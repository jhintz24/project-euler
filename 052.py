
def containSameDigits(a, b, c, d, e):
    return sorted(str(a)) == sorted(str(b)) == sorted(str(c)) == sorted(str(d)) == sorted(str(e))

def ansFunction():
    x = 1
    while True:
        if containSameDigits((2*x), (3*x), (4*x), (5*x), (6*x)):
            return x
        x += 1

print ansFunction()