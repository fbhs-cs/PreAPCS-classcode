import random
total = 0
NUM_TRIALS = 10

for i in range(NUM_TRIALS):
    sum = 0
    num_to_one = 0

    while sum < 1:
        sum += random.random()
        num_to_one += 1
    total += num_to_one

avg_num_to_one = total / NUM_TRIALS
print(avg_num_to_one)
