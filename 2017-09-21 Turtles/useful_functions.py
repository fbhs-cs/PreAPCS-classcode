'''Some functions you may find useful for your artwork
'''

import turtle

tom = turtle.Turtle()


def color_circle(t, r, c):
    '''draw a circle with radius, r, then fill it in with color, c
    '''
    t.color(c)
    t.begin_fill()
    t.circle(r,90)
    t.end_fill()
    t.ht()  #hides the turtle
 
def color_rectangle(t, l, w, c):
    '''draw a rectangle with length, l, width, w, then fill it in with color, c
    '''
    t.color(c)
    t.begin_fill()
    for i in range(2):
        t.fd(l)
        t.rt(90)
        t.fd(w)
        t.rt(90)
    t.end_fill()
    t.ht()  #hides the turtle


def color_spiral(t, s, c):
    '''draw a spiral with spiralyness of s and color c
    '''
    t.color(c)
    t.speed(0)
    for i in range(100):
        t.circle(s*i, 90)
    

'''you can use a lot of different colors
   others can be found at https://www.w3schools.com/colors/colors_names.asp
'''
def color_demo(t):
    t.color('red')
    t.dot(200)
    t.color('blue')
    t.dot(150)
    t.color('maroon')
    t.dot(100)
    t.color('fuchsia')
    t.dot(50)


'''uncomment the lines below here one at a time to see what each function above does
'''
#color_circle(tom,50,'red')
#color_rectangle(tom,200,70,'blue')
#color_spiral(tom, 2, 'dodgerblue')
#color_demo(tom)
