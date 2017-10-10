def get5():
    num1 = int(input( "Number 1: " ))
    num2 = int(input( "Number 2: " ))
    num3 = int(input( "Number 3: " ))
    num4 = int(input( "Number 4: " ))
    num5 = int(input( "Number 5: " ))

    print( "Total is", num1 + num2 + num3 + num4 + num5 )
    
def while1():
    num = 1
    while num <= 99:
        print(num,end=' ')
        num += 2
    print('done')

def while2(how_many):
    total = 0
    count = 0
    while count < how_many:
        total += int(input('Number {}:'.format(count+1)))
        count += 1
    average = total / count
    print('Total is',total)
    print('Average is',average)


def while3():
    num = int(input('Enter a number: '))
    total = 0
    while num != 0:
        total += num
        num = int(input('Enter a number: '))
    print('Total is',total)



def infinite():
    num = 1
    total = 0
    while(num*num) % 1000 != 0:  #num*num % 1000 is NEVER 0
        total += num
    print("Total is",total)



