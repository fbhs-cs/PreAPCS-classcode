word1 = 'hello'
word2 = 'jello'
count = 0
for letter in word1:
    if letter in word2:
        count+=1
print(count)