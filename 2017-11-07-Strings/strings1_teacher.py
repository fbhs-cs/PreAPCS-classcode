#concatenation

##word = 'example'
##print(word[0])
##print(word[1])
##print(word[2])
##print(word[3])
##print(word[4])
##print(word[5])
##print(word[6])

def spell(word):
    for i in range(len(word)):
        print(word[i])
        
def reverse(word):
    for i in range(-1,-len(word)-1,-1):
        print(word[i])

def spell2(word):
    for letter in word:
        print(letter)
    
def ducks():
    prefixes = 'JKLMNOPQ'
    suffix = 'ack'
    for letter in prefixes:
        if letter == 'O' or letter == 'Q':
            print(letter + 'u' + suffix)
        else:
            print(letter + suffix)


