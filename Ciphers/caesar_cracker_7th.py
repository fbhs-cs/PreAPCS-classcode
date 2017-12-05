from caesar_cipher_7th import encrypt_decrypt

def caesar_cracker(message):
    for i in range(1,26):
        print('Key {}:'.format(i))
        print(encrypt_decrypt(message,i,False))
        print()
