import time
import os

play = True
while play:
    os.system('clear')
    room = 0

    while room != 3:
        
        if room == 0:
            print()
            print('You are in a dark dungeon.')
            print('There is a pathway to your "right" and to your "left"')
            direction = input('Which way do you want to go? ')
            if direction == 'right':
                room = 1
         
            elif direction == 'left':
                room = 2

            else:
                print('There is no path that way!')
        
        if room == 1:
            print()
            print('You are in another dark passage.')
            print('There is a closed door.')
            direction = input('Do you want to "open" it, or go "back"? ')
            if direction == 'open':
                room = 3
            
            elif direction == 'back':
                room = 0
            
            else:
                print('That wasn\'t an option!')
        
        if room == 2:
            print()
            print('You are in a library.')
            print('There is an open book on the table.')
            print('Do you want to "read" the book, ')
            direction = input('or go "back" the way you came? ')
            if direction == 'read':
                room = 0
                print('The book is called, "Trapped in a Dungeon"')
                print('It seems pretty interesting.')
                time.sleep(3)
                print('Suddenly, ')
                time.sleep(2)
                print('you feel yourself being')
                time.sleep(2)
                print('sucked into the pages')
                time.sleep(2)
                print('of the book!')
                time.sleep(4)
                print('Everything goes black...')
                time.sleep(1.5)
                os.system('cls')
                time.sleep(5)
            
            elif direction == 'back':
                room = 0
            
            else:
                print('That is not an option!')
    print()
    print('You find yourself in a classroom.')
    print('It looks like maybe a Computer Science class.')
    print('Your teacher looks at you patiently waiting')
    print('for you to continue working on your story')
    print('project that was assigned on Friday.')
    time.sleep(6)
    while True:
        print()
        again = input('Play again? (yes/no)')
        if again == 'yes':
            room = 0
            break
        elif again == 'no':
            print('Ok, get to work!')
            play = False
            break
        else:
            print("That is not an option!")
        
