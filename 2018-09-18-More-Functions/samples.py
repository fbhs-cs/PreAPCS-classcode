'''
    Monday, September 18, 2017
    Sample code
'''

def do_twice(f):
    f()
    f()
    
    
def print_spam():
    print('spam')
    

#def print_twice(word):
    # code goes here
    
    
#def do_four():
    #code goes here

do_twice(print_spam)




####UNCOMMENT BELOW########
##def center(word):
##    space_size = 35 - len(word)//2
##    print(' '*space_size + word)
##    
##center('hello')
##center('this is a test!')
##center('this should appear in the center')
