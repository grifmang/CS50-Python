import string

def ceasar(plainText, key):
    # plainText = raw_input('Enter the phrase to encrypt: ')
    lower_index = 0
    upper_index = 0
    result = ''
    lower_alpha = string.ascii_lowercase
    upper_alpha = string.ascii_uppercase
    for char in plainText:
        if char.isalpha():
            if char.isupper():
                upper_index = upper_alpha.index(char)
                encrypted = upper_index + key
                if encrypted > 25:
                    encrypted %= 26
                result += upper_alpha[encrypted]
            elif char.islower():
                lower_index = lower_alpha.index(char)
                encrypted = lower_index + key
                if encrypted > 25:
                    encrypted %= 26
                result += lower_alpha[encrypted]
        else:
            result += char
        encrypted = 0
    print result

ceasar('Be sure to drink your Ovaltine!', 13)