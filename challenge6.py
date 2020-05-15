#write a function that accepts a sentence as an argument
#and checks how many times a word appears in it.

# STEPS.
# 1. Split sentence into a list of words
# 2. create a placeholder to count the number of repetitions. Set it to 0
# 3. Iterate through the list of words
#       - check if the current item is equals to the word we're counting. If yes, increment count by 1. If not, ignore

love = "i love my cat Nala. Nala is a good kitty."

def word_count(sentence , word):
    word_list = sentence.split(" ")
    count = 0

    for item in word_list:
        if item.lower() == word.lower():
            count += 1
    return count


print(word_count(love , "nala"))
