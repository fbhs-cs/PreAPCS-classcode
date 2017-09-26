import turtle

tip = turtle.Turtle()

tip.seth(90)

def draw_bar():
    tip.fd(25)
    tip.bk(50)
    tip.fd(25)

def draw_plus():
    draw_bar()
    tip.rt(90)
    draw_bar()
    tip.lt(90)
    
def draw_part():
    draw_plus()
    tip.fd(50)
    draw_plus()
    tip.bk(100)
    draw_plus()
    tip.fd(50)
    
def draw_flake():
    draw_part()
    tip.rt(90)
    draw_part()
    tip.lt(90)
    
draw_flake()