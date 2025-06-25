options = ['rock', 'paper', 'scissors']

def right_word(word):
    return word in options

def get_word_from_user():
    word = input('Choose rock, paper or scissors. ')
    #while not right_word(word):
        #word = input('Try again!\n')
    #return word

    #return word if right_word(word) else get_word_from_user()

get_word_from_user()