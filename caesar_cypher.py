def caesar_cipher(message,key,mode):
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    translated = ''
    message = message.upper()
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            if mode == 'encrypt':
                num += key
            elif mode == 'decrypt':
                num -= key
                
            num %= len(LETTERS)
            
            translated = translated + LETTERS[num]
        else:
            translated = translated + symbol

    return(translated)


def main():
    while True:
        mode = input('Would you like to encrypt or decrypt?')
        valid_answers = ['encrypt','decrypt','e','d']
        if mode in valid_answers:
            break
        else:
            print('Invalid option.')
        
    while True:
        try:
            key = int(input('Encryption Key: '))
            break
        except:
            print('The key must be an integer.')
    
    if mode == 'e':
        mode = 'encrypt'
    elif mode == 'd':
        mode = 'decrypt'
    
    if mode == 'encrypt':
        message = input('Enter plain text message: ')
        print('Your encrypted message is:')
        print(caesar_cipher(message,key,mode))
    elif mode == 'decrypt':
        message = input('Enter cipher text: ')
        print('Your decrypted message is:')
        print(caesar_cipher(message,key,mode))
    

if __name__ == '__main__':
    main()
    
    
    