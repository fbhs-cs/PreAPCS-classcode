"""This is a sample solution for the
    "Top Down Design" activity in class
"""
import turtle

bob = turtle.Turtle()
bob.seth(90)
bob.speed(0)

def draw_piece():
    bob.fd(25)
    bob.rt(180)
    bob.fd(50)
    bob.rt(180)
    bob.fd(25)
    
def draw_plus():
    draw_piece()
    bob.rt(90)
    draw_piece()
    bob.lt(90)
    
def draw_branch():
    bob.fd(75)
    draw_plus()
    bob.bk(75)

def draw_snowflake():
    draw_branch()
    bob.rt(90)
    draw_branch()
    bob.rt(90)
    draw_branch()
    bob.rt(90)
    draw_branch()
    bob.rt(90)
    
draw_snowflake()
