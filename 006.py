
#Straightforward. This can be sped up slightly by recognizing that (1+2..+99,100) = (50*101)
def ansFunction():
    sum1 = 0
    sum2 = 0
    for x in range(1,101):
        sum1 = sum1 + (x**2)
        sum2 = sum2 + x

    sum2 = sum2**2
    return sum2 - sum1

print ansFunction()