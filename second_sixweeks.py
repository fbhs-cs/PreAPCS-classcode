def func1(x):
    count = 0
    while count <= x:
        print(count)


def func2(x):
    for i in range(1,10,2):
        print(i)
    
    
def func3(x, y):
    sum = 0
    for i in range(x):
        if i % y == 0:
            sum += i
    return sum


def func4(x):
    if len(x) > 1:
        return ''
    elif len(x) > 5:
        return x[:5]
    
    
def func5(x):
    for i in range(len(x)):
        print(x[i],end=' ')
        
def func6(x):
    for l in x:
        if l > 'a' and l < 'z':
            print(l.upper(),end='')
        elif l > 'A' and l < 'Z':
            print(l.lower(),end='')
        else:
            print(l)
            
            
def func7(x):
    return '!!' + x[:] + '!!'
    
    
    
def count_vowels(word):
    count = 0
    vowels = 'aeiou'
    for letter in word:
        if letter in vowels:
            count += 1
        
