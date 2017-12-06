from caeser_cipher import encrypt_decrypt

def caeser_crack(message):
    for i in range(1,26):
        print('Key #{}: '.format(i) + encrypt_decrypt(message, i, 'D'))
    

def main():
    while True:
        message = input('What is your encrypted message?\n> ')
        print('--------Possible Decryptions--------')
        caeser_crack(message)
        again = input('Do you have another message to decrypt? (y/n)\n> ')
        if again.lower() == 'y':
            continue
        elif again.lower() == 'n':
            return
        
if __name__ == '__main__':
    main()