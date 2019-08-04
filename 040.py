
def ansFunction():
    d = ''
    x = 1
    while True:
        d += str(x)
        if len(d) >= 1000000:
            break
        x += 1

    return int(d[0]) * int(d[9]) * int(d[99]) * int(d[999]) * int(d[9999]) * int(d[99999]) * int(d[999999])

print ansFunction()