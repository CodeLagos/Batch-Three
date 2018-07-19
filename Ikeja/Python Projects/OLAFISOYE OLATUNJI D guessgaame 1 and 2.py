#Please help remove the bulk commenting

#This is a guess the number game.
'''
import random

GuessNumber = 0

print ("Hello player, what is your name?: ")  #Ask for player's name
myName = input()    #Player inputs hiss/her name
print ("Nice name " +myName+ "!, Welcome to the 'Guess the number game'")
number = random.randint(1, 40) #numbers with the range 1 - 40

#Notiifying the user the range to guess the number
print ("hmmm, ", myName, "I am thinking of a number between the range of 1 to 40.")

#The player's choice
print("Are you sure you can guess the number? Y/ N: ")

answer = input()
if answer == str("N"):
        print ("Please do visit us another time, Thanks " +myName)
        
if answer != str("Y") and answer != str("N"):
    print ("Invalid Character, Game Aborted")

if answer == str("Y"):
    while GuessNumber < 1:
        print ("Take a guess.")
        guess = input()
        guess = int (guess)
        GuessNumber = GuessNumber + 1

        if guess < number:
            print ("Your guess is too low!, try again " +myName)
          
        if guess > number and guess > 40:
            print ("Try again")
        if guess > 41:
            print ("You are beyond the guess range! enter number less or equal to 40")
        if guess == number:
            break
        if guess == number:
            guessNumber = str("Guess Accepted")
            print ("Weldone " +myName+ "You are a Genious")

        if guess != number:

            number = str(number)
            print ("Oops! The number I was thinking of was " +number)



#using the sleep function to make it looks like booting

import random
import sys
from time import sleep

def gen_number():
    random_number = random.randint(1, 21) #generating a random number btw 1 - 21
    return random_number

def intro(): #introduction aspect, making the game looks real!
    print ("Welcome to the 'GUESS THE NUMBER GAME'!")
    print ("Guess a number within the range of 1 - 20")
    print ()
    
def ask_number(question, random_number):
    answer = None
    while answer != random_number:
        try:
            answer = int(input(question))
            if answer < random_number:
                print ("Lower")
            elif answer > random_number:
                print ("Higher")
            elif answer == random_number:
                sleep(3)
                print ("Calculating..........!")
                print ("Bravo!")
                
        except ValueError:
            print ("Invalid! Enter a number between 1 - 21")
            return answer
def player_guess ():
    print ("Player, Let's begin")
    sleep (2)
    random_number = gen_number()

    guess = ask_number ("Guess the number:  ", random_number)

def congrat_winner (answer, random_number):
    if answer == random_number:
        print ()
        print ("Calculating result........")
        sleep (2)
        print ()
        print ("Weldone!")
        print ("The answer is correct!")
        replay_game()
        
def replay_game():
    replay_question = None
    while replay_question != str("Y") and replay_question != str("N"):
               replay_question = input ("Would you like to try again? (Y/ N): ") .lower()
               if replay_question == str("Y"):
                   print ()
                   print ("restarting the game....")
                   main()
               elif replay_question == str("N"):
                   print ("Goodbye")
               exit()
               
    else:
               print ("Enter either Y or N: ")
def main():
            intro()
            player_guess()
            congrat_winner()
            replay_game()

main()
'''
#Please note, the last block of code isn't well smooth. help fix lil error and send to
#my email address, glottyweb@gmail.com
