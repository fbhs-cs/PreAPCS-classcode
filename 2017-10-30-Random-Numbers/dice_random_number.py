from random import randint

num_of_zeros = 0
num_of_ones = 0
num_of_twos = 0
num_of_threes = 0
num_of_fours = 0
num_of_fives = 0
num_of_sixes = 0
num_of_sevens = 0
num_of_eights = 0
num_of_nines = 0
NUM_TRIALS = 100
for trial in range(NUM_TRIALS):
    sum_of_ten = 0
    for i in range(10):
        die = randint(1,6)
        #print(die)
        sum_of_ten += die
    #print(sum_of_ten)
    rand = sum_of_ten % 10
    if rand == 1:
        num_of_ones += 1
    elif rand == 2:
        num_of_twos += 1
    elif rand == 3:
        num_of_threes += 1
    elif rand == 4:
        num_of_fours += 1
    elif rand == 5:
        num_of_fives += 1
    elif rand == 6:
        num_of_sixes += 1
    elif rand == 7:
        num_of_sevens += 1
    elif rand == 8:
        num_of_eights += 1
    elif rand == 9:
        num_of_nines += 1
    elif rand == 0:
        num_of_zeros += 1
    else:
        print("ERROR") # THIS SHOULD NEVER HAPPEN

print('''If the numbers generated are random, there
should be about the same number of each digit showing
up.''')
print('------------RESULTS FOR {} TRIALS------------'.format(NUM_TRIALS))
print('''0s: {:3}  1s: {:3}  2s: {:3}  3s: {:3}  4s: {:3}
5s: {:3}  6s: {:3}  7s: {:3}  8s: {:3}  9s: {:3}'''\
      .format(num_of_zeros, num_of_ones, num_of_twos,\
              num_of_threes,num_of_fours,num_of_fives,\
              num_of_sixes,num_of_sevens,num_of_eights,\
              num_of_nines))

                                                              
                                                              