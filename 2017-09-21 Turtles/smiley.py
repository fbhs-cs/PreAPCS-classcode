import turtle

tom = turtle.Turtle()


def draw_face(t, xpos, ypos, size, color):
    """Draws the circle for a smiley face at position (xpos, ypos) with
       a diameter of size and with the given color.  t is a turtle.
    """
    t.penup()
    t.goto(xpos, ypos)
    t.dot(size, color)
    t.pendown()

def draw_eye(t, xpos, ypos):
    """Draws a black eye at (xpos, ypos). t is a turtle.
    """
    t.penup()
    t.goto(xpos,ypos)
    t.dot(50)
    t.pendown()

def draw_smile(t,xpos, ypos):
    """Draws a smile with its center at (xpos, ypos).  t is a turtle.
    """
    t.seth(0)
    t.penup()
    t.goto(xpos,ypos)
    t.pendown()
    t.circle(100,90)
    t.penup()
    t.goto(xpos,ypos)
    t.pendown()
    t.seth(180)
    t.circle(-100,90)

def draw_smiley_face(t,xpos, ypos, size, color):
    """Draws a smiley face at (xpos, ypos) with a diameter of size and
       face color, color. t is a turtle.
    """
    draw_face(t, xpos, ypos, size, color)
    draw_eye(t, xpos-size//5, ypos+size//5)
    draw_eye(t, xpos+size//5, ypos+size//5)
    draw_smile(t, xpos, ypos-size//3)
    t.ht()


draw_smiley_face(tom, -200, 0, 400, 'yellow')
draw_smiley_face(tom, 200, 0, 400, 'green')