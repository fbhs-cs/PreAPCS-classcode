
print("Let's play Hangman.")



# set the secret word here
secret_word = 'secret word'

# creates a variable with an empty value
guesses = ''

# determines the number of guesses allowed
turns = 10


while turns > 0:
    # count how many letters aren't found
    not_found = 0
    
    for char in secret_word:
        
        #see if the character is in the player's guesses
        if char in guesses:
            print(char,end='')
        else:
            # if the character isn't found, print an underscore and increase not_found
            print('_',end='')
            not_found += 1
    
    # if not_found == 0 all characters were found and the game is over
    if not_found == 0:
        print()
        print('You Won!')
        break
    
    print()
    
    #ask the player to guess a character
    valid_guess = False
    while not valid_guess:
        guess = input('Guess a letter: ')
        if len(guess) == 1:
            valid_guess = True
        else:
            print('Invalid guess.')
    # add the player's guess to guesses
    guesses += guess
    
    # if the guess is not found in the word
    if guess not in secret_word:
        turns -= 1
        print("Wrong")
        
        # display how many turns are left
        print("You have",turns,"more guesses.")
        
        # if turns are equal to 0 the game is over
        if turns == 0:
            print('You lose.')
        
    
    
        


