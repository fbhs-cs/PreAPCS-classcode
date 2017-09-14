
#This is a one-line comment
'''This is a longer comment that can
   continue over multiple lines.  We will use
   this type of comment to describe many of
   the functions that we create'''

#Assignment statements
n = 17
first = 'bob'
last = 'smith'
birth_date = '9/27/2003'

#Variable names
'''variable names should be lowercase
   connect multiple words with _
   variables names CANNOT start with a number,
       or a special character ie. @,#,!, etc.
'''
# 14thname = 'dakota'   THIS IS NOT ALLOWED!

#Keywords
# class = '7th' THIS IS NOT ALLOWED
'''class is a KEYWORD'''
''' if elif return while FULL LIST ON page 10'''

#Expressions and statements
'''Expressions'''
16 % 2
3 + 3
n + 5

'''Statements'''
n = 25
print(n)
print('hello')

#Order of operations
print('P - parentheses')
print('E - exponents')
print('MD- multiplication or division (left to right)')
print('AS- addition or subtraction (left to right)')
#Basic string operations
name = first + ' ' + last #concatenation
print(name)

print('{} {}'.format(first, last))

length = 4
width = 5
area = length * width
print('The area of a rectangle with width {} and length {} is {}'.format(width, length, area))
#Types of errors
x = 42 # This works!
# 42 = x  Syntax error!

'''Semantic/Logic error'''
length = 12
width = 15
area = length + width  #WRONG FORMULA
print(area)
