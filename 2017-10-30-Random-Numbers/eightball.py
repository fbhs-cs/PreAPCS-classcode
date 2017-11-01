from random import randint

print('Welcome to the Magic Eight Ball')
while True:
    print('Think of a yes/no question, then press <enter>')
    input()
    num = randint(1,4)
    if num == 1:
        print('Yes, for sure.')
    elif num == 2:
        print('No, absolutely not.')
    elif num == 3:
        print('I can\'t tell for sure.')
    elif num == 4:
        print('Definitely.')
    #TODO MORE RESPONSES
        # 1 POSITIVE RESPONSES
        # 2 UNSURE RESPONSES
        # 2 NEGATIVE RESPONSES
        
    print('Do you have more questions? (y/n)')
    again = input('> ').lower()
    if again == 'n':
        break
   
    