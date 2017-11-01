for player in range(3):
    for computer in range(3):
        diff = player - computer
        result = diff % 3
        print('Player: {}\tComputer: {}\tResult: {}'.format(player,computer,result))
