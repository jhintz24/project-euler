
#Helper function from problem 004
def isPalindrome(n):
    n = str(n)
    if n == n[::-1]:
        return True
    else:
        return False

def ansFunction(n):
    palindromes = []
    for x in range(n):
        if isPalindrome(x):
            base2 = bin(x)[2:]
            if isPalindrome(base2):
                palindromes.append(x)

    return sum(palindromes)

print ansFunction(1000000)