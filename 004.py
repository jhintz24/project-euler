def isPalindrome(n):
    n = str(n)
    if n == n[::-1]:
        return True
    else:
        return False

def largestPalindrome():
    n1 = 999
    n2 = 999
    while True:
        x = n1 * n2
        if isPalindrome(x):
            return x


