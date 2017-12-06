from caesar_cipher import encrypt_decrypt

def cesar_cracker(message):
    for i in range(1,26):
        print('Key {:2}:' .format(i) + encrypt_decrypt(message,i,False))
        print()
        
def main():
    run = True
    while run:
        message = input('Input a message: ')
        cesar_cracker(message)
        while True:
            again = input('Do you have another message to decrypt? (y/n) ')
            if again == 'Y' or again == 'y':
                run = True
                break
            elif again == 'N' or again == 'n':
                run = False
                print('Thanks, have a nice day!')
                break
            else:
                print('Please enter y or n')

if __name__ =='__main__':
    main()