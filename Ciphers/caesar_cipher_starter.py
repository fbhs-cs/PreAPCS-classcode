''' File...Save As...caesar_cipher.py'''
run = True
while run:
    while True:
        mode = input('(E)ncrypting or (D)ecrpyting? ')
        if mode == 'E' or mode == 'e':
            encrypting = True
            break
        elif mode == 'D' or mode == 'd':
            encrypting = False
            break
        else:
            print('Please enter "E" or "D".')
    message = input("What is your message? ")
    while True:
        try:
            key = int(input("What is your key? "))
            break
        except:
            print('The key must be an integer.')
                  
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

    if encrypting:
        print('Encrypted text: ')
    else:
        print('Decrypted text: ')
    print(out_text)
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


