'''
Guess a letter on what the mystery word is and if it's wrong you lose a life.
Keep going until you either guessed the word or you lost all your lives. 

1) import random
2A) Create a list of words and call it 'mystery_words' or 'msytWords'
    2B) For now, list <=10 words to keep it simple, then gradually increase it
3A) ask the user to enter their name and guess a letter
    3B) if the user enter a capital letter, use the lower method
    3C) if enetered special char (!@?^) or numb (12345), ask the user to enter a letter
    3D) if enter a word, tell/ask the user to enter a single letter
4) Create a while loop for the gme to keep goin until user decides to stop
 Incorrect_guesses = [] and correct_guesses = []


'''

import random

mystery_words = ['apple', 'banana', 'code', 'python', 'axe']
