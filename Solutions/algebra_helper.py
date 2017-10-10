import math

def find_slope(x1,y1,x2,y2):
    dy = y2 - y1
    dx = x2 - x1
    slope = dy/dx
    print('The slope of the line through ({}, {}) and ({}, {}) is {:.1f}'.format(x1,y1,x2,y2,slope))

def find_eq(x1,y1,x2,y2):
    dy = y2 - y1
    dx = x2 - x1
    slope = dy/dx
    b = y1 - slope*x1
    print('The equation of the line through ({}, {}) and ({}, {}) is y = {:.1f}x + {:.1f}'.format(x1,y1,x2,y2,slope,b))
 

def find_dist(x1,y1,x2,y2):
    dy = y2 - y1
    dx = x2 - x1
    dist = math.sqrt(dy**2 + dx**2)
    print('The length of the segment with endpoints ({}, {}) and ({}, {}) is {:.1f}'.format(x1,y1,x2,y2,dist))
    
def find_mid(x1, y1, x2, y2):
    midx = (x1 + x2) / 2
    midy = (y1 + y2) / 2
    print('The midpoint of the segment with endpoints({}, {}) and ({}, {}) is ({}, {})'.format(x1,y1,x2,y2,midx,midy))


def main():
    print('Welcome to the Algebra Helper!')
    print("I'm here to help, but first I need some information:")
    name = input('What should I call you? ')
    print("Ok {}, let's get started!".format(name))
    print("All I need from you are two coordinates (x1, y1) and (x2, y2)")
    x1 = float(input('x1 = '))
    y1 = float(input('y1 = '))
    x2 = float(input('x2 = '))
    y2 = float(input('y2 = '))
    find_slope(x1,y1,x2,y2)
    eq = find_eq(x1,y1,x2,y2)
    find_dist(x1,y1,x2,y2)
    find_mid(x1,y1,x2,y2)
    
 
   
    
main()

