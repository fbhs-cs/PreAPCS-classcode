from random import randint

x=0
while x != :
    x = randint(1,10)
    print(x)


def times_table():
    '''Prompts for a number and then prints a times table from 1 to 10 for that number
    '''
    val = int(input('Enter a number:'))
    num = 1
    while num <= 10:
        prod = num * val
        print("{:2} * {} = {:3}".format(num,val,prod))
        num += 1

def sum_average():
    '''Prompts for numbers until 0 is entered
       then displays their sum and average
    '''
    num = -1
    total = 0
    count = -1  #first time through the loop
                #count gets set to 0
    while num != 0:
        count += 1
        num = int(input('Enter a number:'))
        total += num
    if count == 0:
        average = 0
    else:
        average = total / count
    print('Total is',total)
    print('Average is',average)

def countdown(num):
    '''Counts down from a given num to 1 then Blast off!
    '''
    while num > 0:
        print(num)
        num -= 1
    print('Blast off!')



