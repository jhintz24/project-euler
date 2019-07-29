
def ansFunction(n):
    num = str(2**n)
    ans = 0
    for digit in num:
        ans = ans + int(digit)

    return ans

print ansFunction(1000)