from random import randint

def play_hand():
    pc1 = randint(1,10)
    pc2 = randint(1,10)
    dc1 = randint(1,10)
    dc2 = randint(1,10)

    psum = pc1 + pc2
    dsum = dc1 + dc2
    print('You drew {} and {}.'.format(pc1,pc2))
    print('Your total is {}'.format(psum))
    print()
    print('The dealer has {} and {}'.format(dc1,dc2))
    print('Dealer\'s total is {}.'.format(dsum))
    print()

    while dsum == psum:
            print('TIE! Time for a tie-breaker:')
            npc = randint(1,10)
            ndc = randint(1,10)
            print('You drew {}.'.format(npc))
            print('Dealer drew {}.'.format(ndc))
            psum += npc
            dsum += ndc
            print()
    if psum > dsum:
        print('YOU WIN!')
    elif psum < dsum:
        print('YOU LOSE!')

def play_again():
    print('Play again? y/n')
    ans = input('> ').lower()
    if ans == 'y':
        return True
    else:
        return False
    
def play_game():
    print('Welcome to Baby Blackjack!\n')
    play_hand()
    while play_again():
        play_hand()
    
play_game()
