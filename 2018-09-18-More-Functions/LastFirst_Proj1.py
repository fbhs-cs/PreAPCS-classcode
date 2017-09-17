#NAME:
#DATE:
#PERIOD:


'''Project1

Write a function draw_3x3 that calls other functions to create a grid like the one below.
Note: Your draw_3x3 function should have no print statements in it.

+ - - - + - - - + - - - +
|       |       |       |
|       |       |       |
|       |       |       |
+ - - - + - - - + - - - +
|       |       |       |
|       |       |       |
|       |       |       |
+ - - - + - - - + - - - +
|       |       |       |
|       |       |       |
|       |       |       |
+ - - - + - - - + - - - +

To print more than one value on a line, you can print a comma-
separated sequence of values:

	print('+','-')

Print will advance to the next line, unless you override that behavior:

	print('+', end=' ')   #will put a blank space at the end.
	print('-')

The output of these statements is '+ -' on the same line.  
'''

##Helper Functions.  You may use these, but will also need to#
##create some helper functions of your own.
def do_three(f):
	f()
	f()
	f()
	
def print_beam():
	print('+ - - -',end=' ')

def print_bar():
	print('|      ',end=' ')
	
	

##############################################################

def draw_3x3():

	#Start your code here


