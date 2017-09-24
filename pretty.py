import turtle
import random

def animate():
    while True:
        colors = ['red','blue','green','purple','yellow']
        t = turtle.Turtle()
        t.speed(10)
    
        for i in range(180):
            t.color(random.choice(colors))
            t.forward(200)
            t.right(30)
            t.forward(40)
            t.left(60)
            t.forward(100)
            t.right(30)
        
            t.penup()
            t.setposition(0,0)
            t.pendown()
        
        
            t.right(2)
        t.reset()
        
animate()