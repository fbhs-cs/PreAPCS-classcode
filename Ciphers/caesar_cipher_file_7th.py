from caesar_cipher_7th import encrypt_decrypt

def decrypt_file(in_file,out_file,key):
    try:
        f = open(in_file)
        text = f.read().splitlines()
        f.close()
    except FileNotFoundError:
        print('File not found.')
        return
    except:
        print('Something bad happened.')
        return
    
    print('Decrypting...')
    f = open(out_file,'w')
    for line in text:
        f.write(encrypt_decrypt(line,key,False)+'\n')
    f.close()
    print('Done.')
      
def main():
    in_file = input('Enter input file name: ')
    out_file = input('Enter output file name: ')
    key = int(input('Enter key: '))
    decrypt_file(in_file,out_file,key)
    
if __name__ == '__main__':
    main()
