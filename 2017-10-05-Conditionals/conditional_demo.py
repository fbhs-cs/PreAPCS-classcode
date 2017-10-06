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
    

def main():
    shape = input('What shape? (square or triangle) ')
    
    if shape != 'triangle' and shape != 'square':
        print("That's not an option!!")
        return
    
    side_length = int(input("Side length? "))
    
    if shape == 'triangle':
        print("Here's your triangle!")
        triangle(side_length)
    elif shape == 'square':
        print("Here's your square!")
        square(side_length)
    
        
        
    
    
    
main()