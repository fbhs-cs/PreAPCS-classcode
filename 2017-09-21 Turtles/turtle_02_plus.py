#NAME:
#DATE:
#PERIOD:

"""DO NOT EDIT ANYTHING IN THIS SECTION"""
import turtle

t = turtle.Turtle()
t.seth(90)

def moveForward():
    t.fd(50)
    
def turnLeft():
    t.lt(90)
    
"""-----------------------------------"""
""" Define a function called turn_around which turns the turtle around."""






""" Define a function called draw_plus that uses move_forward() and turn_around()
to draw a plus sign that is centered at the turtles starting location.
Note: the turtle should end where it started, which is in the middle of the
plus sign, facing up.
"""










""" Define a function called right() that uses turn_left() to make the turtle turn right. """










"""Use your function right() and the move_forward() function to define a function draw_rectangle()
that draws a rectangle."""








"""Define a function draw_nxn_rectangle that has two parameters: length and width that draws
a rectangle with the given dimensions."""







"""MAIN METHOD (USE FOR TESTING)"""
def main():
    t.reset()
    t.goto(-200,200)
    draw_plus()
    t.penup()
    t.goto(200,200)
    t.pendown()
    draw_rectangle()
    t.penup()
    t.goto(0,-200)
    t.pendown()
    draw_nxn_rectangle(5,3)
    
#main()