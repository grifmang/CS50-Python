import string

def vigenere():
    while True:
        key = input('Please enter a key string: ')
        
        if not key:
            print('Key cannot be blank.')
            continue
        elif not key.isalpha():
            print('Only letters in the key, please.')
            continue
        
        break
        
    while True:
        plaintext = input('Please enter a string to encrypt: ')
        
        if not plaintext:
            print('Enter a string to encrypt please.')
            continue

        break
    
    lower_index = 0
    upper_index = 0
    result = ''
    lower_alpha = string.ascii_lowercase
    upper_alpha = string.ascii_uppercase
    counter = 0
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                upper_index = upper_alpha.index(char)
                if counter >= len(key):
                    counter = 0
                encrypted = upper_index + upper_alpha.index(key[counter].upper())
                if encrypted > 25:
                    encrypted %= 26
                result += upper_alpha[encrypted]
                counter += 1
            elif char.islower():
                lower_index = lower_alpha.index(char)
                if counter >= len(key):
                    counter = 0
                encrypted = lower_index + lower_alpha.index(key[counter])
                if encrypted > 25:
                    encrypted %= 26
                result += lower_alpha[encrypted]
                counter += 1
        else:
            result += char
        encrypted = 0
    
    print(result)
    return result

        
            
vigenere()
            