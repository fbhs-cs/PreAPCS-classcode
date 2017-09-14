

def old_mac():
    print('Old Macdonald had a farm')

def eieio():
    print('Ee I ee I oh!')
    
def on_that(animals, sound):
    print('And on that farm he had some {}'.format(animals))
    eieio()
    print('With a {}-{} here'.format(sound, sound))
    print('And a {}-{} there'.format(sound, sound))
    print('Here a {}, there a {}'.format(sound,sound))
    print('Everywhere a {}-{}'.format(sound,sound))

def open_close():
    old_mac()
    eieio()
    
def verse(animals,sound):
    open_close()
    on_that(animals,sound)
    open_close()
    print()
    
def sing():
    verse('cows','moo')
    verse('chickens','cluck')
    verse('pigs','oink')

sing()