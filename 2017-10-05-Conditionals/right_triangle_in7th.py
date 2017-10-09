def is_right(a,b,c):
    if a<=0 or b<=0 or c <=0:
        print('Invalid side length!')
        return
    longest = max(a,b,c)
    
    if longest == c:
        legs_squared = a**2 + b**2
    elif longest == a:
        legs_squared = c**2 + b**2
    else:
        legs_squared = a**2 + c**2
    
    hyp_squared = longest**2
    
    if legs_squared == hyp_squared:
        print('It is right!')
    else:
        print('It is NOT right!')
        
is_right(-3,-4,-5)
is_right(3,4,6)
is_right(5,4,3)