from random import randint

nums = 10*[0]
NUM_TRIALS = 100000
for trial in range(NUM_TRIALS):
    sum_of_ten = 0
    for i in range(10):
        die = randint(1,6)
        #print(die)
        sum_of_ten += die
    #print(sum_of_ten)
    rand = sum_of_ten % 10
    nums[rand] += 1

print('''If the numbers generated are random, there
should be about the same number of each digit showing
up.''')
print('------------RESULTS FOR {} TRIALS------------'.format(NUM_TRIALS))
for i in range(10):
    if i == 5:
        print()
    print('{}s: {:5}'.format(i,nums[i]),end='\t\t')  

                                                              
                                                              