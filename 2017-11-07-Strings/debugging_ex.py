def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False
   
    i = 0
    j = len(word2)-1
    while j >= 0:
        print(i,j)
        if word1[i] != word2[j]:
            return False
        i = i+1
        j= j-1
    return True

def is_palindrome(word):
    if len(word) == 0:
        return False
    i = 0
    j = len(word) - 1
    while j >= 0:
        if word[i].lower() != word[j].lower():
            return False
        i = i+1
        j = j-1
    return True


def what_is_after(word,letter):
    num_times = word.count(letter)
    is_at = -1
    for i in range(num_times):
        is_at = word.find(letter,is_at+1)
    return word[is_at+1:]