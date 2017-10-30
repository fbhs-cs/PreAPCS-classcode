from random import randint

print('Welcome to the Magic Eight Ball')
while True:
    print('Think of a yes/no question, then press <enter>')
    input()
    num = randint(1,3)
    if num == 1:
        print('Yes, for sure.')
    elif num == 2:
        print('No, absolutely not.')
    elif num == 3:
        print('I can\'t tell for sure.')
    #TODO MORE RESPONSES
        # 3 POSITIVE RESPONSES
        # 3 UNSURE RESPONSES
        # 3 NEGATIVE RESPONSES
        
    print('Do you have more questions? (y/n)')
    again = input('> ')
    #TODO check if they typed in y or n
    break
    