#access libraries and py files
import time
import os 
import spiderDraw as sd
import functions as md


#Initialize variables and setup 
#Need to keep track of correct letters, incorrect letters and tries

correct = []  #List of correct letters guessed
incorrect = []  #List of incorrect letters guessed
tries = 0   #Number of incorrect guesses
game = True 

#Make a list of the spider drawings
spiderList = [sd.spider_0, sd.spider_1, sd.spider_2, sd.spider_3, sd.spider_4, sd.spider_5, sd.spider_6]

limit = len(spiderList) - 1 

def play_game():
  word = md.generate_word()   
  correct = []  #List of correct letters guessed
  incorrect = []  #List of incorrect letters guessed
  tries = len(incorrect)   #Number of incorrect guesses
  #game = True
  #tries == limit 



#Game Loop
#run_game()
#while keep_playing
# 
while game:
  time.sleep(1)
  os.system('clear') # clear screen

  print(md.print_word(word, correct))
  md.print_wrong_guesses(incorrect)  
  md.print_spider(tries,spiderList)
  guess = input('Guess a letter:\n')
  correct, incorrect = md.check_word(guess, correct, incorrect)






  '''
  if not md.is_guess_vaild(guess):
    print('You only need one letter. Enter again\n')
    continue

  if md.already_guessed(guess, correct, incorrect):
    print('Already guessed that letter. Try again!')
    continue

  if md.is_correct_guess(guess, word):
    correct.append(guess)
    print('Yep, correct!')
  else:
    incorrect.append(guess)
    print('Incorrect, my friend!')

  break
  '''

  #This is where you'll call all of your functions. Just need to decide the proper order.


  #You will also need to specify your win and lose conditions in here