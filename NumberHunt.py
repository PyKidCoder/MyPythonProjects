#In this assignment you have to guess the number between 1 and 100
#and this program try to guess your number

import random 


#n will hold any random value between 1 and 100
n = random.randint(1, 100)

#You have to guess the number between 1 to 100
print('I have selected a number between 1 and 100. Can you guess?')

#attempt variable will hold the count of your guess
attempts = 0

#done is boolean variable and will hold true or false
done = False

#the while loop is the main part of the code, it lets us guess the number as per the hints
while not done:
  #guess variable with hold guess number
  guess = int(input('Guess the number\n'))
  attempts = attempts + 1
  
  if guess > n:
    print('My number is smaller than that.\n')
      
  if guess < n:
    print('My number is larger than that.\n')
    
  if guess == n:
    print('Yay, that is correct.')
    print('You took ', attempts, 'attempts to guess it.')
    done = True

print()
print()
done = False

print('Now your chance. You select a number between 1 and 100')
print('Click enter when ready')

#Here python is going to guess the number
input()


guess = 0
attempts = 0
guess_step = 10; 

#in this code it turnes the guess step to 10 meaning it will jump on to number in 10,20...
prev_answer = '0'

while not done:
    
    answer = input('Is it '+ str(guess) + '? (y = Yes, s = smaller than that, l = larger than that) \n')
    attempts = attempts + 1 

    if attempts > 1: 
      if answer != prev_answer:
       
        guess_step = guess_step - 1
      
    prev_answer = answer
  
    if answer.lower() == 's':
        guess = guess - guess_step
    
    if answer.lower() == 'l':
        guess = guess + guess_step
    
    if answer.lower() == 'y':
      print (' Yay, I got it.')
      print('I took ', attempts, 'attempts to guess it.')
      done = True
    

print()
print()

print('I think I can do it smarter ... ')
print('Let me try binary search ... ')

#Here python is going to try to guess the number in less attempts than the first try 
#using Binary Search
done = False
low = 0
high = 100
guess_step = 0
attempts = 0

while not done:
    guess = round((low + high)/2)
    answer = input('Is it '+ str(guess) + '? (y = Yes, s = smaller than that, l = larger than that) \n')
    attempts = attempts + 1 

    if answer.lower() == 's':
        high = guess
    
    if answer.lower() == 'l':
        low = guess
    
    if answer.lower() == 'y':
      print('Bingo, I got it.')
      print('I took ', attempts, 'attempts to guess it.')
      done = True
    
print()
print()
