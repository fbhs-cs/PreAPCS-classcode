import os

while True:

    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    print('You are startled awake...',end='')
    input()
    print('You look around the room and see a door and a window.')
    print('Do you want to walk out through the (d)oor or\nclimb out of the (w)indow?')
    choice = input('Your choice:')
    if choice == 'd':
        print('You walk through the door and are greeted by adoring fans!')
        print('You must be a rock star or something...',end='')
        input()
        print('One of your fans comes up to you with their hand inside')
        print('their coat.  It might be a gun or a knife!')
        print('Do you want to (p)unch the fan or (h)ug the fan?')
        choice = input('Your choice:')
        if choice == 'p':
            print('You take a wild swing at the fan, but instead of hitting')
            print('the fan, you hit the very large, burly, man next to them.')
            print("He doesn't look pleased...")
            input()
            
        elif choice == 'h':
            print('You open your arms wide to hug the fan.  They suddenly pull')
            print('out a rubber chicken and offer it to you.  That\'s strange...')
            input()
            
        continue
    elif choice == 'w':
        print('You forgot you were on the 40th story of your hotel...')
        print('As you fall, you wonder if this is what it feels like to')
        print('be a sperm whale...',end='')
        input()
        continue
    elif choice == 'stop':
        print('You didn\'t say the magic word...',end='')
        input()
        continue
    elif choice == 'quit':
        print('Quitters never win and winners never quit!')
        input()
        continue
    elif choice == 'pinch me':
        print('Ouch! That hurt!')
        print('You open your eyes, feeling refreshed.\nWow, what a strange dream!')
        break
    else:
        print('Tired...Confused...you go back to sleep...',end='')
        input()
        continue
    
