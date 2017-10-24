import os
from random import randint

def branch1():
    print('You are startled awake...',end='')
    input()
    print('You look around the room and see a door and a window.')
    print('Do you want to walk out through the (d)oor or\nclimb out of the (w)indow?')
    choice = input('Your choice:')
    if choice == 'd':
        print('You walk through the door and are greeted by adoring fans!')
        print('You must be a rock star or something...',end='')
        input()
        return True
        
    elif choice == 'w':
        print('You forgot you were on the 40th story of your hotel...')
        print('As you fall, you wonder if this is what it feels like to')
        print('be a sperm whale...',end='')
        input()
        return False
    elif choice == 'stop':
        print('You didn\'t say the magic word...',end='')
        input()
        return False
    elif choice == 'quit':
        print('Quitters never win and winners never quit!')
        input()
        return False
    else:
        print('Tired...Confused...you go back to sleep...',end='')
        input()
        False
    
def branch2():
    print('One of your fans comes up to you with their hand inside')
    print('their coat.  It might be a gun or a knife!')
    print('Do you want to (p)unch the fan or (h)ug the fan?')
    choice = input('Your choice:')
    if choice == 'p':
        print('You take a wild swing at the fan, but instead of hitting')
        print('the fan, you hit the very large, burly, man next to them.')
        print("He doesn't look pleased...")
        input()
        return False
            
    elif choice == 'h':
        print('You open your arms wide to hug the fan.  They suddenly pull')
        print('out a rubber chicken and offer it to you.  That\'s strange...')
        input()
        return True
    
    else:
        print('By doing nothing, you have accepted your fate.')
        print('The adoring fan grips you in a massive bear hug.')
        print('As you drift out of consciousness, you wonder if')
        print('this could have been prevented in some way...')
        return False

def branch3():
    print('Before you get a chance to do anything, a security')
    print('guard rushes from out of nowhere and grabs the rubber')
    print('chicken out of the fan\'s hand. ')
    print('Do you want to (c)ommend the security guard, or')
    print('(s)cold the security guard?')
    choice = input('Your choice:')
    print()
    if choice == 'c':
        print('After telling the guard thank you and shaking her hand,')
        print('you are lauded in the press for being such a great and')
        print('down to earth celebrity.  Everyone buys your next album')
        print('and you go down in history as the best rock star in the')
        print('history of mankind...')
        input()
        return True
    if choice == 's':
        print('After scolding the guard, security guards refuse to')
        print('work for you anymore.  Without security, all of your')
        print('upcoming tour dates are cancelled.  Without the world')
        print('tour, your album sales plummet and your fans all start')
        print('talking about you as a one-hit wonder.')
        print('You can\'t help but wonder if this could have been prevented')
        print('somehow...')
        input()
        return False
    else:
        print('Your security detail sees your inaction as non support.')
        print('They go on strike.  Without security, all of your')
        print('upcoming tour dates are cancelled.  Without the world')
        print('tour, your album sales plummet and your fans all start')
        print('talking about you as a one-hit wonder.')
        print('You can\'t help but wonder if this could have been prevented')
        print('somehow...')
        input()
        return False
def branch4():
    print('You need to withdraw some money from the ATM.')
    print('Due to your stardom, there is plenty of cash in your')
    print(' account, now if only you could remember your pin...')
    tries = 0
    pin = str(randint(1000,9999))
    while tries < 5:
        guess = input('Enter your 4 digit security pin ({} tries left):'.format(5 - tries))
        if guess == pin:
            print('That was it!  You withdraw $1,000,000 and head to the mall.')
            input()
            return True
        else:
            print('That didn\'t work...')
            tries += 1
    print('You suddenly remember your PIN! It was {}',format(pin))
    print('Unfortunately, you have locked yourself out of your account')
    print('for 24 hours. Unable to access your fortune,')
    print('you withdraw from society, wallow in self-pity,')
    print('and go to bed without eating dessert.')
    input()
    return False

def end():
    input('You are startled awake...')
    input('woah deja vu...')
    print('You were dreaming about something, but can\'t seem')
    print('to remember what.  Oh well, you feel well rested')
    print('and ready to start your day.  You have an audition')
    print('in an hour, you better hurry up!')
    
def main():    
    while True:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        
        if not branch1():
            continue
        print()
        if not branch2():
            continue
        print()
        if not branch3():
            continue
        print()
        if not branch4():
            continue
        print()
        end()
        break
        
if __name__ == '__main__':
    main()
    
    
    
