#access libraries and py files
import time
import os 
import spiderDraw as sd
import functions as md

#Initialize variables and setup 
#Need to keep track of correct letters, incorrect letters and tries
spiderList = [sd.spider_0, sd.spider_1, sd.spider_2, sd.spider_3, sd.spider_4, sd.spider_5, sd.spider_6]



def play_game():
  #time_limit = 5 * time_in_mins
  # time_when_started

    
  correct = []  #List of correct letters guessed
  incorrect = []  #List of incorrect letters guessed
  tries = len(incorrect)    #Number of incorrect guesses
  limit = len(spiderList) - 1   #game = True
  md.introduction()
  word = md.generate_word() 

  #Game Loop

  while True: #not md.won_game(word, correct) and not md.lost_game(incorrect):

    time.sleep(1)
    os.system('clear') # clear screen

    
    print(md.print_word(word, correct))
    md.print_wrong_guesses(incorrect)  
    md.print_spider(len(incorrect),spiderList)
    guess = input('Guess a letter:\n')
    correct, incorrect = md.check_word(guess, correct, incorrect, word)
    #print(word)

    if md.won_game(correct, word):
      print('Hooray! You win!\n')
      break
    
    if md.lost_game(incorrect):
      print(f'Correct word: {word}')
      break

    

    

play_game()

  