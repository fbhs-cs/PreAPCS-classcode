import math
def trans_encrypt(message, key):
    out_list = ['']*key
    
    for i in range(len(message)):
        out_list[i%key] += message[i]
    return ''.join(out_list)

def trans_decrypt(message, key):
    num_cols = key
    num_rows = math.ceil(len(message)/key)
    num_shaded = key - len(message) % key
    out_list = [''] * num_rows
    row = 0
    col = 0
    for char in message:
        out_list[row] += char
        if (row == num_rows - 1) or (row == num_rows-2 and col >= num_cols - num_shaded):
            row = 0
            col += 1
        else:
            row += 1 
    return ''.join(out_list)

m = 'This is a test message'
m = trans_encrypt(m,5)
print("Encrypted: "+m)
m = trans_decrypt(m,5)
print("Decrypted: "+m)