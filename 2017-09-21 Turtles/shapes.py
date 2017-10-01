import turtle
import math
tuesday = turtle.Turtle()

def square(t,length):
    polygon(t, length, 4)

def polygon(t, length, n):
    poly_line(t,length,360/n,n)
        
def circle(t, r):
    arc(t, r, 360)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length/3)+3
    piece_length = arc_length / n
    piece_angle = angle / n
    poly_line(t,piece_length,piece_angle,n)

def poly_line(t,length,angle,n):
    for i in range(n):
        t.fd(length)
        t.rt(angle)
        

    
    
