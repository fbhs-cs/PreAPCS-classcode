
def is_right(a, b, c):
    longest = max(a,b,c)
   
    if c == longest:
        s_squared = a**2 + b**2
        l_squared = c**2
    elif a == longest:
        s_squared = c**2 + b**2
        l_squared = a**2
    else:
        s_squared = a**2 + c**2
        l_squared = b**2
     
    if s_squared == l_squared:
        print('It IS a right triangle!')
    else:
        print('It IS NOT  a right triangle!')

