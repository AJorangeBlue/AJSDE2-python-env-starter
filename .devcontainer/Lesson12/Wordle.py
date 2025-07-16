import time
import random
import os
#Wordle Clone Outline
#Follow comments to help build out your game

#Set Up Game Variables. We will need variables to:
#store the number of guesses the player has made
#store the different colors we want to use
#keep track of letters that were guessed in the correct position
#letters guessed that were in the incorrect position 
#letters guessed that were not in the word at all.
# https://github.com/Gspidie/SDE2-python-env-starter-GSP/blob/main/ArachnoPhonics%20Game%20Project.py/main.py







#Create your Welcome message that explains how the game works
def introduction():
    print('\nWelcome to Wordle!\nYour goal is to guess the hidden word in 5 tries.')
    print('Each word is 5 letters long, and depending on what letter you guess,')
    print('You will get feedback on whether the letter is in that word.')
    print(f'If the letter is in \033[32mGreen\033[0m, it\'s in the correct position.')
    print(f'\033[33mYellow\033[0m means the letter is in there, but not in the right position.')
    print(f'\033[31mRed\033[0m means it\'s not in the word at all.\n')
    user_name = input('Before we start, What\'s your name?\n')
    print(f'Hi {user_name}! Let the game(s) begin!\n')




#Generate Word Function. Opens a word list file, then chooses a word at random


def generate_word():
    wordList = open('.devcontainer/Lesson12/words_for_wordle.txt').read().split()
    word = random.choice(wordList)
    print('Word = ' + '_'*len(word))
    #print(word)  # For debugging purposes, remove this line in final version
    return word.lower() #lowercase for consistency



#Get User Guess Function. Prompts user for a guess, checks to make sure it is a 5 letter word
def user_guess():
    while True: # checks if the guess has only 5 letters
        guess = input('Enter a 5 letter word:\n').lower()
        if len(guess) == 5 and guess.isalpha(): # This was suggested by Ai but changed to to length of guess
            return guess
        else:
            print('That\'s not a valid word. Try again!')
            #time.sleep(1) # Error message pops up for a second and clears the screen
            #os.system('clear')



#Compare Words Function. Compares the word guessed by the player to the solution word 
# generated at random earlier. Needs to check if each letter of the guess is in the solution word, 
# and if so, if it is in the correct position or not. Then it will print out the guess word again, 
# with each letter colored to reflect whether it was wrong, correct letter but wrong position, or 
# completely correct.

def compare_words(guess, accurate):
    guess_in_color = ''
    for i, letter in enumerate(guess):
        if letter == accurate[i]: # Green = correct letter & position
            guess_in_color += f'\033[32m{letter}\033[0m' 
        elif letter in accurate: # Yellow = correct letter incorrect position
            guess_in_color += f'\033[33m{letter}\033[0m'
        else: 
            guess_in_color += f'\033[31m{letter}\033[0m'
    return guess_in_color




#Print Letters Function - Prints the entire alphabet for the user, coloring all letters that have been 
# guessed so far to reflect if those letters were 1. Not in the word at all, 2. 
# In the word but wrong position or 3. In the word and correct position
def print_word(guess, accurate):
    print(f'{compare_words(guess, accurate)}')





#Game Loop. Calls the functions. Checks for win or lose conditions. 
# Wins if all letters are in the correct place and there are less than 5 guesses.
def game_loop():
    correct = []  #List of correct letters guessed
    incorrect = []  #List of incorrect letters guessed
    tries = len(incorrect)    #Number of incorrect guesses
    limit = 5  

introduction()
time.sleep(3)
os.system('clear')
word = generate_word()
guess = user_guess()
compare_words(guess, word)
print('\n')
print_word(guess, word)
