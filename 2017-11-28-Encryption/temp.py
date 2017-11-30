while True:
    try:
        x = int(input('Enter a number: '))
        y = x / 0
        print(x)
        break
    except ZeroDivisionError:
        print('divide by 0')
        break
    except:
        print('Not an int')

print('this is after the try block')