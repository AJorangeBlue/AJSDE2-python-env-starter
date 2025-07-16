'''
U - Largest Prime Factor Finder Make a function that finds the biggest prime factor of a number list. 
 This means breaking the number into smaller parts until you find the biggest prime number among them.

C - Number list, break the numbers into smaller parts, find the biggest prime number in the list

A - 

* import random

* set n equal to 10 
* number_list = creates 10 random number (1-100) with random.choices()

* create function called 'find_big_prime' that takes the list as a parameter
* Inside that function, create variable called 'largest_prime' and set it to '0.'
-This where the prime number will be replaced if it happens to find a much bigger prime num

* Create a for/while loop that goes through each number
* In that loop use an if statement to see if an number is a prime number
Note: A prime number is a number that is only divisible by 1 and itself.

* if random number is divisble by 1 and (&&) the number itself, then do:
	* Compare that number to "largest_prime"
  * if number > "largest_prime", replace number as the largest_prime
* (Optional Else): if random number isn't divisble, then continue 


'''

import random

n = 10
number_list = random.choice(range(2, 101), k=n)

def find_big_prime(number_list):
	largest_prime = 0
  #for i in number_list[i]:
  	