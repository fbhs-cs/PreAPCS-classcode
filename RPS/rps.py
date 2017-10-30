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
        
        
        #Determine who wins -- you DO NOT need to
        #                      fully understand this
        #                      right now but you need
        #                      to understand the scoring
        who_wins = (pc - cc) % 3
        if who_wins == 0:
            print('Draw!')
            continue
        elif who_wins == 1:
            print(turn_explanation(pc,cc))
            print('You win!')
            num_wins += 1  # player wins
            num_games += 1
        elif who_wins == 2:
            print(turn_explanation(pc,cc))
            print('You lose!')
            num_games += 1
        else:
            print('Something went wrong!')
            break
        
        display_score(num_wins,num_games)
        print('Play again? ([y]\\n)')
        again = input('> ').upper()
        if again == 'N':
            #TODO - ADD RESPONSES BASED ON HOW THE PLAYER DID OVERALL
            print('Thanks for playing!')
            break
        else:
            continue



def display_score(wins,total):
    print('-----------Score------------')
    print('Wins: {}         Losses: {}'.format(wins,total - wins))


def turn_explanation(choice1, choice2):
    #TODO ADD OTHER TURN EXPLANATIONS
    if choice1 == 0 or choice2 == 0:
        if choice1 == 1 or choice2 == 1:
            return 'Paper covers Rock.'
        elif choice1 == 2 or choice2 == 2:
            return 'Rock breaks Scissors.'
        
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
    #TODO EXPLAIN RULES
    print('Rules go here.')
    

    
    
    
if __name__ == '__main__':
    play_game()
