'''
Create a function that takes in a string (that contains words and spaces) as a parameter and returns the length of the last word in that string.
Example: If “Hello World” was input, the function would return 5 (for World)
Example: If “We should code with C2C”, the function would return 3 (for C2C)
def last_word_length(sentence):
    # Split the sentence into words
    words = sentence.split()
    # Check if there are any words in the list
    if not words:
        return 0  # Return 0 if there are no words
    # Return the length of the last word
    return len(words[-1])
'''
#def last_word_length(str_sentence):
    #type = input('Enter a string: ')

def last_word_scentence():
    enter = ""
    while True:
        enter = input('Enter a word or a sentence.\n')
        # Remove spaces and check if the rest are all letters
        if enter.replace(" ", "").isalpha():
            words = enter.split()
            print(words)
            break
        else:
            print('That isn\'t valid. Try again.')

last_word_scentence()