'''A program to demonstrate using Turtle graphics to draw an image
'''

import turtle
from random import randint

tom = turtle.Turtle()
screen = turtle.Screen()

def setup(s):
    s.title("A Purdy Picture!")
    s.bgcolor("skyblue")
    s.setup(410,610)  
    
def draw_rectangle(t,length,width,fillcolor):
    t.color(fillcolor)
    t.begin_fill()
    for i in range(2):
        t.fd(length)
        t.rt(90)
        t.fd(width)
        t.rt(90)
    t.end_fill()

def draw_triangle(t,side,fillcolor):
    t.color(fillcolor)
    t.begin_fill()
    for i in range(3):
        t.fd(side)
        t.lt(120)
    t.end_fill()

def draw_ground(t):
    t.pu()
    t.setpos(-205,-205)
    draw_rectangle(t,410,100,"grey")
    
def draw_grass(t):
    t.pu()
    t.setpos(-205,0)
    draw_rectangle(t,410,205,"green")
    t.pd()
    
def draw_barn(t):
    t.pu()
    t.setpos(-100,100)
    draw_rectangle(t,200,200,"red")
    t.pd()
    
def draw_roof(t):
    t.pu()
    t.setpos(-100,100)
    draw_triangle(t,200,"black")
    t.pd()
    
def draw_cloud(t):
    t.pu()
    t.setpos(randint(-150,150),200)
    t.color("white")
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    t.seth(0)
    t.fd(50)
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    t.pd()

def draw_left_window(t):
    t.pu()
    t.setpos(-75,75)
    draw_rectangle(tom,50,75,"white")
    t.pd()
    
def draw_right_window(t):
    t.pu()
    t.setpos(25,75)
    draw_rectangle(tom,50,75,"white")
    t.pd()

def draw_door(t):
    t.pu()
    t.setpos(-25,-25)
    draw_rectangle(tom,50,75,"brown")
    
def draw_wframe(t):
    t.color('black')
    t.width(3)
    for i in range(2):
        t.fd(50)
        t.rt(90)
        t.fd(75)
        t.rt(90)
    t.fd(25)
    t.rt(90)
    t.fd(75)
    t.bk(37)
    t.lt(90)
    t.fd(25)
    t.bk(50)

def draw_left_frame(t):
    t.pu()
    t.setpos(-75,75)
    t.pd()
    draw_wframe(t)

def draw_right_frame(t):
    t.pu()
    t.setpos(25,75)
    t.pd()
    draw_wframe(t)

def draw_knob(t):
    t.pu()
    t.setpos(15,-65)
    t.color("black")
    t.dot(8)
    t.pd()
    
def main():
    tom.speed(2)
    setup(screen)
    draw_ground(tom)
    draw_grass(tom)
    draw_cloud(tom)
    
    draw_roof(tom)
    draw_barn(tom)
    draw_left_window(tom)
    draw_left_frame(tom)
    draw_right_window(tom)
    draw_right_frame(tom)
    
    draw_door(tom)
    draw_knob(tom)
    tom.ht()
    
main()
