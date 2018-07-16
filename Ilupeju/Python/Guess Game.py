##import module
import random
##set the initial variable for the number of guesses
numberofGuesses = 0
##create a particular number to be guessed
number = 50
##create a string for the user to input name
name = str(input("Hello! What is your name? "))

print(name + ", I am thinking of a whole number between 1 and 70. Can you guess what it is?")
##create a loop that repeats while the user guess is not the same as the answer
while numberofGuesses < 6:
  guess = int(input("Take a guess "))
  guess = int(guess)
##Each time through the loop 1 is added to the number of attempts
  numberofGuesses = numberofGuesses + 1;
  guessesLeft = 6 - numberofGuesses;

  if guess < number:
    guessesLeft=str(guessesLeft)
    print("Your guess is too low! You have " + guessesLeft + " guesses left")

  if guess > number:
    guessesLeft=str(guessesLeft)
    print("Your guess is too high! You have " + guessesLeft + " guesses left")

  elif guess==number:
    break
##After the loop it will say how many attempts it took to get the answer.

if guess==number:
  numberofGuesses=str(numberofGuesses)
  print("Good job! You guessed the number in " + numberofGuesses + " tries :)")

elif guess!=number:
  number=str(number)
  print("Sorry. The number I was thinking of was " + number + " :)")
