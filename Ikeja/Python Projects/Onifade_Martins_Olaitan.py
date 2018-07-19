# Guess Game done by Onifade Martins olaitan

import random
def guess_the_number():
   guessesTaken = 0
   print('Hello! What is your pet name?')
   myName = input()
   print('Well ' +myName+ " Give me two numbers, a min and a max") #The player gets to pick two numbers
   x = int(input("Select min. "))
   y = int(input("Select max. "))

   number = random.randint(x,y) #The computer chooses a random number between the numbers x & y
   print('Well, ' + myName + ', I am having a number between your min & max in mind ' )
   while guessesTaken < 10:
      print('Take a guess.')
      guess = input()
      guess = int(guess)
      guessesTaken = guessesTaken + 1
      if guess < number:
         print('Your guess is too low, try harder.')
      if guess > number:
         print('Your guess is too high, keep trying.')

      if guess == number:
         break

   if guess == number:
      guessesTaken = str(guessesTaken)
      print('Excellent, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

   if guess != number:
      number = str(number)
      print('Nope! You have run out of guesses, The number I was thinking of was ' + number)

guess_the_number()
