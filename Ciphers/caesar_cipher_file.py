from caesar_cipher_4th import encrypt_decrypt


def main():
    
    # open the file holding the message to be encrypted or decrypted
    while True:
        in_filename = input('File name to encrypt/decrypt: ')
        try:
            f = open(in_filename)
            text = f.readlines()
            f.close()
            break
        except:
            print('File not found.')
    
    while True:
        out_filename = input('File name to store the result: ')
        try:
            f = open(out_filename,'w')
            break
        except:
            print('Invalid file')
    
    while True:
        try:
            key = int(input('Key: '))
            break
        except:
            print('The key must be an integer.')
    
    while True:
        print('(E)ncrypting or (D)ecrypting {}?'.format(in_filename))
        mode = input('> ')
        if mode.upper() == 'E' or mode.upper() == 'D':
            break
        else:
            print('Please enter E or D')
            
    print('Working...')
    for line in text:
        f.write(encrypt_decrypt(line,key,mode.upper()))
    
    f.close()
    print('All done!')
            

if __name__ == '__main__':
    main()