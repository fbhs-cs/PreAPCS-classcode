'''
    Monday, September 18, 2017
    Sample code
'''

##def do_twice(f):
##    f()
##    f()
##    
##    
##def print_spam():
##    print('spam')
##    
##def print_two():
##    print(2)
##    
##def print_twice(word):
##    print(word)
##    print(word)
##    
##    
##def do_four(func):
##    do_twice(func)
##    do_twice(func)
##
###do_twice(print_spam)
###do_twice(print_two)
##do_four(print_spam)
###print_twice('hornets')




####UNCOMMENT BELOW########
def center(word):
    space_size = 35 - len(word)//2
    print(' '*space_size + word)
    
center('hello')
center('this is a test!')
center('this should appear in the center')
