
#Helper function from problem 004
def isPalindrome(n):
    n = str(n)
    if n == n[::-1]:
        return True
    else:
        return False

def ansFunction(n):
    count = 0
    for x in range(1,n):
        z = x
        for y in range(1, 50):
            z = z + int(str(z)[::-1])
            if isPalindrome(z):
                break
        else:
            count += 1

    return count

print ansFunction(10000)
