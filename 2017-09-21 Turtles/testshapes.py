""" Test file for 'mypolygon.py' with the following functions:

    square(t, length)
        t: Turtle
        length: length of sides
        
    polygon(t, length, n)
        t: Turtle
        length: length of sides
        n: number of sides
        
    circle(t, r)
        t: Turtle
        r: radius
        
    arc(t, r, angle)
        t: Turtle
        r: radius
        angle: angle subtended by the arc
"""

from shapes import *
import turtle

tom = turtle.Turtle()
tom.speed(0)

def moveTurtle(t,x,y):
    t.pu()
    t.setpos(x,y)
    t.pd()
    t.seth(0)
    
"""Draw square in the center of the screen"""
square(tom,length=100)

"""Draw a pentagon in the top left of the screen"""
moveTurtle(tom,-300,200)
polygon(tom,length=100,n=5)  


"""Draw a circle in the top right of the screen"""
moveTurtle(tom,300,200)
circle(tom,r=50)


"""Draw semi-circle in the bottom left of the screen"""
moveTurtle(tom,-300,-200)
arc(tom,r=50,angle=180)


"""Draw an octagon in the bottom right of the screen"""
moveTurtle(tom,300,-200)
polygon(tom,50,8)