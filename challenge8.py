# Create a function that takes a string and removes spaces around it. 
# Create a function that takes a sentence and removes spaces around it.
# It also transforms any word in Capital letters into upper case.
# Example:
# ```py
# remove_spaces(' my name is FIFI') 
# ```
# should return `my name is Fifi`

name = " My name is FIFI. "
def remove_spaces(sentence):
    words = sentence.split() #splits sentence at every space.
    list_words = []
    
    for word in words:
        if word.isupper() == True:
            new_word = word.casefold()
            list_words.append(new_word) #Python Casefold() method returns a lowercase copy of the string.
        else:
            list_words.append(word)
    new_sentence = " ".join(list_words)
    
    print(new_sentence)    

remove_spaces(name)
