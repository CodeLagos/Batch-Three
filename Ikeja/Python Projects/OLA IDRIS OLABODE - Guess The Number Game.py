# This is a guess the number game.

import random
def guess_the_number():
   guessesTaken = 0
   print('Hello! What is your name?')
   myName = input()
   print('Well ' +myName+ " Give me two numbers, a min and a max") #The user gets to pick two numbers
   a = int(input("Select min. "))
   b = int(input("Select max. "))

   number = random.randint(a,b) #The computer chooses a random number between the numbers a & b
   print('Well, ' + myName + ', I am thinking of a number between your min & max')
   while guessesTaken < 6:
      print('Take a guess.')
      guess = input()
      guess = int(guess)
      guessesTaken = guessesTaken + 1
      if guess < number:
         print('Your guess is too low.')
      if guess > number:
         print('Your guess is too high.')

      if guess == number:
         break

   if guess == number:
      guessesTaken = str(guessesTaken)
      print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

   if guess != number:
      number = str(number)
      print('Nope! You have run out of guesses, The number I was thinking of was ' + number)

guess_the_number()
