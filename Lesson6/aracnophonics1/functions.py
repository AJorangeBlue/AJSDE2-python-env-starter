import random


# Prompts user for letter guess. Checks through the secret word to see if it contains the letter guessed by the user. Returns the number of wrong guesses
#Takes in the correct letter list, incorrect letter list, secret word and the number of tries as parameters.

def check_word(guess, correct, incorrect, word):
  if not is_guess_vaild(guess):
    print('You only need one letter. Enter again\n')
    guess = input('Guess a letter:\n')
    return check_word(guess, correct, incorrect, word)
    
  if already_guessed(guess, correct, incorrect):
    print('Already guessed that letter. Try again!')
    return correct, incorrect
  
  if is_correct_guess(guess, word):
    correct.append(guess)
    print('Yep, correct!')
  else:
    incorrect.append(guess)
    print('Incorrect, my friend!')
  
  return correct, incorrect
  
def won_game(correct, word):
  for letter in word:
    if letter not in correct:
      return False
  return True #:)



def lost_game(incorrect):
  if len(incorrect) >= 7:
    print('Oh no, The spider ate you!\nGAME OVER!')
    return True
  return False # :,(


def is_correct_guess(guess, word):
  return guess.lower() in word
  

def is_guess_vaild(guess):
  #any 1 letter regardless of casting
  return guess.isalpha() and len(guess) == 1

def print_wrong_guesses(incorrect):
  result = 0
  print('Incorrect Guesses = ' + ', '.join(incorrect))
  #print(f'Incorect = {', '.join(incorrect)}')


# Returns the word to the console containing "_" for any letter not guessed by the user.
#Takes in the correct word and the list of correct guesses as parameters
def print_word(word, correctGuesses):
  word = 'word = '
  for i, letter in enumerate(correctGuesses):
    if letter not in correctGuesses:
      word += '_'
    else: word += letter
  return word
  



# Prints spider from the spider drawing functions in the spiderDraw.py file. Takes the number of wrong guesses and the list of spider drawing functions as parameters.

def print_spider(tries,spiderList):
  spiderList[tries]()
  
    



#Opens the word list text file, stores the contents into a list, chooses a random word from the list, finds the length of that word and prints a string of blanks for each letter in the word. Returns the word.
def generate_word():
  wordList = open('Lesson6/aracnophonics1/words.txt').read().split()
  word = random.choice(wordList)
  print('Word = ' + '_'*len(word))
  return word

def already_guessed(guess, incorrectG, correctG):
  return ((guess in incorrectG) or (guess in correctG))
  

#Put the introduction code/input player name into here 
def introduction():
  print('\nWelcome to my game of Spider Hang!')
  name = input('What is your name?\n')
  print(f'Hello {name}, we\'re gonna play a little game..')