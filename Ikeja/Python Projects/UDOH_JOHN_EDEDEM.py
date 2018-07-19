
#GUESS NUMBER GAME.

import random

guessesTaken = 0

print("WHAT'S UP DOCK!!! Your name please...YOU HAVE 5 ATTEMPTS")
myName = input()

Number = random.randint(0,10)
print(myName + ', GUESS a number between 1 and 10.')

while guessesTaken < 5:

    guess = int(input("Please enter your guess:"))

    guessesTaken = guessesTaken + 1

    if guess > Number:
        print('Guess is too HIGH...TRY AGAIN')
    if guess < Number:
        print('Guess too LOW...TRY AGAIN')

    if guess == Number:
        break
if guess == Number:
    guessesTaken = str(guessesTaken)
    print('CONGRATULATIONS!!!, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

if guess != Number:
    Number = str(Number)
    print("SORRY!!! The CORRECT number is " + Number)

