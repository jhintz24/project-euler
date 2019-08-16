
def decryptText(cipherText):
    for a in range(97,123):
        for b in range(97,123):
            for c in range(97,123):
                decryptedText = []
                key = chr(a) + chr(b) + chr(c)
                longKey = ''
                index = 0
                while len(longKey) < len(cipherText):
                    longKey += key[index]
                    if index == len(key) - 1:
                        index = 0
                    else:
                        index += 1

                for i in range(len(cipherText)):
                    decryptedText.append(chr(cipherText[i] ^ ord(longKey[i])))

                decryptedText = ''.join(decryptedText)
                if 'An extract taken from the introduction' in decryptedText: #First I filtered for common English words like 'the', 'and', 'is' and excluded chars like '|' and '{'
                    print longKey
                    print decryptedText
                    sum = 0
                    for char in decryptedText:
                        sum += ord(char)
                    return sum





cipherText = []
with open('input-files/p059_cipher.txt') as f:
    for line in f:
        cipherText.extend(map(lambda x: int(x),line.strip('\n').split(',')))

print cipherText

print decryptText(cipherText)