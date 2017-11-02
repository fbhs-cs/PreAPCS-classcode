from random import randint
import time

AUTHOR = 'Your Name'

def play_game():
    
    print('Welcome to Rock, Paper, Scissors.')
    print('Programming by Mr. Purdy and {}'.format(AUTHOR))
    
    while True:
        print('Do you need an explanation of the rules? (y/n)')
        rules = input('> ')

        if rules.lower() == 'y':
            show_rules()
            break
        elif rules.lower() == 'n':
            print('Ah, an expert!')
            break
        else:
            print('Sorry, I didn\'t catch that.')
            continue
    
    #Start game here
    num_wins = 0
    num_games = 0
    while True:
        #Get player choice
        print('(R)ock, (P)aper, or (S)cissors?')
        player_choice = input('> ').upper() # make their choice uppercase
        if player_choice == 'R':
            pc = 0
        elif player_choice == 'P':
            pc = 1
        elif player_choice == 'S':
            pc = 2
        else:
            print('Try again.')
            continue
        
        #Get computer choice
        cc = randint(0,2)
        
        #Translate the numbers into words
        pmove = move_name(pc)
        cmove = move_name(cc)
        
        #Visually show game play 
        for i in range(1,4):
            print('{}...'.format(i))
            time.sleep(0.5)
        print('Shoot!')
        time.sleep(0.5)
        print('You chose: {}       Computer chose: {}'.format(pmove, cmove))
        
        
        #Determine who wins
        who_wins = (pc - cc) % 3
        if who_wins == 0:
            print('Draw!')
            continue
        elif who_wins == 1:
            print(turn_explanation(pc,cc))
            print('You win!')
            num_wins += 1  # player wins, add 1 to their score
            num_games += 1
        else:
            print(turn_explanation(pc,cc))
            print('You lose!')
            num_games += 1
        
        
        display_score(num_wins,num_games)
        print('Play again? ([y]\\n)')
        again = input('> ').upper()
        if again == 'N':
            num_losses = num_games - num_wins
            if num_wins > num_losses:
                print('Great job!')
            else:
                print('Better luck next time!')
            print('Thanks for playing!')
            break
        else:
            continue



def display_score(wins,total):
    print('-----------Score------------')
    print('Wins: {}         Losses: {}'.format(wins,total - wins))


def turn_explanation(choice1, choice2):
    if choice1 == 0 or choice2 == 0:
        if choice1 == 1 or choice2 == 1:
            return 'Paper covers Rock.'
        elif choice1 == 2 or choice2 == 2:
            return 'Rock crushes Scissors.'
    else:
        return 'Scissors cuts Paper.'
    
            
            
        
        
def move_name(num):
    if num == 0:
        return 'Rock'
    elif num == 1:
        return 'Paper'
    elif num == 2:
        return 'Scissors'
    else:
        return 'Invalid'


def show_rules():
    print('Choose Rock, Paper, or Scissors.')
    print('Rock beats Scissors.')
    print('Paper beats Rock.')
    print('Scissors beats Paper.')
    print('Play as long as you like,')
    print('and try to beat your previous')
    print('score!')
    

    
    
    
if __name__ == '__main__':
    play_game()
