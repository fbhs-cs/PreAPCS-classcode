'''
Encryption Algorithm
1. Decide on a key from 1 to 25.
2. Find the plaintext letter's number
3. Add the key to the plaintext letter's number
4. If this number is larger than 26, subtract 26.
5. Find the letter for the number calculated. This
   is the cipher text letter.
6. Repeat steps 2 to 5 for every letter in the plaintext
   message.
'''
mode = input('(E)ncrypting or (D)ecrpyting? ')
if mode == 'E':
    encrypting = True
elif mode == 'D':
    encrypting = False
message = input("What is your message? ")
key = int(input("What is your key? "))
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
cipher_text = ''
for plain_letter in message:
    if plain_letter.upper() in LETTERS:
        index = LETTERS.find(plain_letter.upper())
        if encrypting:
            new_index = index + key
        elif not encrypting:
            new_index = index - key
        new_index = new_index % 26
        cipher_letter = LETTERS[new_index]
        cipher_text += cipher_letter
    else:
        cipher_text += plain_letter

print(cipher_text)
'''
Decryption Algorithm
1. Given a key from 1 to 25.
2. Find the ciphertext letter's number
3. Subtract the key from the ciphertext letter's number
4. If this number is negative, add 26.
5. Find the letter for the number calculated. This
   is the plaintext letter.
6. Repeat steps 2 to 5 for every letter in the ciphertext
   message.
'''

