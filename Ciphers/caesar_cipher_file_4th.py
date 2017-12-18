from caesar_cipher_4th import encrypt_decrypt

def decrypt_file(in_file,out_file,key):
    try:
        f = open(in_file)
        text = f.read().splitlines()
        f.close()
    except:
        print('That file does not exist.')
        return
    print('Decrypting {}...'.format(in_file))
    f = open(out_file,'w')
    for line in text:
        f.write(encrypt_decrypt(line,key,"D")+'\n')
    f.close()
    print('Done.')
def main():
    in_file = input('Enter input filename: ')
    out_file = input('Enter output filename: ')
    key = int(input('Enter the key: '))
    decrypt_file(in_file,out_file,key)
    
if __name__ == '__main__':
    main()
