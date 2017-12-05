
def encrypt_decrypt(message, key, mode):
    ''' encrypts or decrypts message using key
        mode = E or mode = D
    '''
    if mode == 'E':
        encrypting = True
        
    elif mode == 'D':
        encrypting = False
        
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    out_text = ''
    for letter in message:
        if letter.upper() in LETTERS:
            index = LETTERS.find(letter.upper())
            if encrypting:
                new_index = index + key
            elif not encrypting:
                new_index = index - key
            new_index = new_index % 26
            out_text += LETTERS[new_index]
        else:
            out_text += letter
    return out_text


def main():
    run = True
    while run:
        while True:
            mode = input('(E)ncrypting or (D)ecrpyting? ')
            if mode == 'E' or mode == 'e':
                mode = 'E'
                break
            elif mode == 'D' or mode == 'd':
                mode = 'D'
                break
            elif mode == 'Q' or mode == 'q':
                return
            else:
                print('Please enter "E" or "D" or "Q" to quit.')          
      
        message = input("What is your message? ")
        while True:
            try:
                key = int(input("What is your key? "))
                break
            except:
                print('The key must be an integer.')
                      
        
        
        if mode == 'E':
            print('Encrypted text: ')
            print(encrypt_decrypt(message,key,mode))
        else:
            print('Decrypted text: ')
            print(encrypt_decrypt(message,key,mode))
        
        while True:
            again = input('Do you have another message to encrypt/decrypt? (y/n) ')
            if again == 'Y' or again == 'y':
                run = True
                break
            elif again == 'N' or again == 'n':
                run = False
                print('Thanks, have a nice day!')
                break
            else:
                print('Please enter y or n')

if __name__ == '__main__':
    main()
    
    
    
    
    
