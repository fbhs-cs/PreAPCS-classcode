import turtle

tina = turtle.Turtle()

tina.seth(90)  #Make tina face forward

def draw_step():
    tina.fd(25)
    tina.lt(90)
    tina.fd(25)
    tina.rt(90)
    
#draw_step()

def draw_side():
    draw_step()
    draw_step()
    draw_step()
    tina.fd(25)
    tina.rt(90)

def draw_diamond():
    draw_side()
    draw_side()
    draw_side()
    draw_side()
    
draw_diamond()