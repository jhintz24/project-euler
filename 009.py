
#Brute force search. No clever math needed
def ansFunction(n):

    for a in range(1,n-1):
        for b in range(a+1,n):
            c = n - a - b
            if a**2 + b**2 == c**2:
                return a*b*c

print ansFunction(1000)