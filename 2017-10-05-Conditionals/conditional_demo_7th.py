import turtle

t = turtle.Turtle()

def square(side):
    for i in range(4):
        t.fd(side)
        t.rt(90)
        
def triangle(side):
    for i in range(3):
        t.fd(side)
        t.rt(120)
        
shape = input('What shape? (square or triangle)')
if shape != 'square' or shape != 'triangle':
    print("That's not an option!")
    

side_length = int(input('Side length?'))

if shape == 'square':
    square(side_length)
    print("Here's your square!")

elif shape == 'triangle':
    triangle(side_length)
    print("Here's your triangle!")

    
    
    



