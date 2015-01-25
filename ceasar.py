import string

def ceasar(plainText):
    # plainText = raw_input('Enter the phrase to encrypt: ')
    lowerIndex = 0
    upperIndex = 0
    result = ''
    lowerAlpha = string.ascii_lowercase
    upperAlpha = string.ascii_uppercase
    for char in plainText:
        if char.isalpha() == True:
            if char.isupper() == True:
                upperIndex = upperAlpha.index(char)
                encrypted = upperIndex + 13
                if encrypted > 25:
                    encrypted = encrypted % 26
                result += upperAlpha[encrypted]
            elif char.islower() == True:
                lowerIndex = lowerAlpha.index(char)
                encrypted = lowerIndex + 13
                if encrypted > 25:
                    encrypted = encrypted % 26
                result += lowerAlpha[encrypted]
        else:
            result += char
        encrypted = 0
    print result

ceasar('Be sure to drink your Ovaltine!')