import math

def area(radius):
    '''returns the area of a circle with radius
    '''
    a = math.pi * radius**2
    return a


def absolute_value(x):
    '''returns the absolute value of x
    '''
    if x < 0:
        return -x
    else:
        return x
    

def compare(x, y):
    '''returns 1 if x is greater than  y
       returns 0 if x is equal to y
       returns -1 if x is less than y
    '''
    if x > y:
        return 1
    elif x == y:
        return 0
    elif x < y:
        return -1
    else:
        print('This can\'t happen!')
      
def distance(x1,y1,x2,y2):
    '''returns the distance between points (x1,y1) and (x2, y2)
    '''
    dx = x2 - x1
    dy = y2 - y1
    dist = math.sqrt(dx**2 + dy**2)
    return dist


def circle_area(xc,yc,xp,yp):
    '''returns the area of a circle with center at (xc, yc)
       and a point on the perimeter of the circle (xp, yp)
    '''
    radius = distance(xc,yc,xp,yp)
    a = area(radius)
    return a


def is_divisible(x, y):
    '''returns True if x is divisible by y
       and False otherwise
    '''
    if x % y == 0:
        return True
    else:
        return False
    
def sumfirst100_div_by_3():
    '''returns the sum of all numbers less than 100
       that are divisible by 3
    '''
    sum = 0
    for x in range(100):
        if is_divisible(x,3):
            #print(x)
            sum += x       
    return sum
    


def is_between(x,y,z):
    '''returns True if y is between x and z
       that is, x <= y <= z,
       returns False otherwise
    '''
    if x<=y<=z or z<=y<=x:
        return True
    else:
        return False
    

                   


