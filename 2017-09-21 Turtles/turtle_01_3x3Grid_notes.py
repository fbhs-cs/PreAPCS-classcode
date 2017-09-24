import turtle

tom = turtle.Turtle()
tom.shape('turtle')

def fdlt():
    tom.forward(50)
    tom.lt(90)

def square():
    fdlt()
    fdlt()
    fdlt()
    fdlt()

tom.color('skyblue')
square()
tom.penup()
tom.forward(100)
tom.pendown()
tom.color('red')
square()
