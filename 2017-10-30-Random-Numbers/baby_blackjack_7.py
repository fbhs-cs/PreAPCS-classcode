from random import randint

def play_hand():
    pc1 = randint(1,10)
    pc2 = randint(1,10)
    dc1 = randint(1,10)
    dc2 = randint(1,10)

    ptotal = pc1 + pc2
    dtotal = dc1 + dc2

    print('You drew {} and {}'.format(pc1,pc2))
    print('Your total is {}.'.format(ptotal))
    print()
    print('The dealer has {} and {}.'.format(dc1,dc2))
    print('Dealer\'s total is {}.'.format(dtotal))
    print()

    while ptotal == dtotal:
        print('TIE!  Running tie-breaker:')
        pnc = randint(1,10)
        dnc = randint(1,10)
        print('You drew {}.'.format(pnc))
        print('Dealer drew {}.'.format(dnc))
        ptotal += pnc
        dtotal += dnc
        print()
        
    if ptotal > dtotal:
        print("YOU WIN!")
    elif ptotal < dtotal:
        print("YOU LOSE!")

def again():
    while True:
        ans = input('Play again? (y/n) ')
        if ans == 'n':
            print('Thanks for playing!')
            return False
        elif ans == 'y':
            return True
        else:
            print('Invalid Answer')
    

def play_game():
    play_hand()
    
    while again():
        play_hand()
        
play_game()