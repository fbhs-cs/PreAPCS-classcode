while True:
    try:
        x = int(input('Enter a number:'))
        y = x / 0
        print(x)
        break

    except ZeroDivisionError:
        print('You cannot divide by 0')
    except:
        print('That was not an int')
