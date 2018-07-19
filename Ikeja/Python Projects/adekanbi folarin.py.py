#the gussing game

print("Hello welcome to guess the number game")
player= input("Enter your name: ")

print ("okay", player, "this is how the game works: ")


print ("The computer randomly generate a number from 1-50,now you have to guess "
"which nunber the computer has choosen and you only have 6 chances."
"At the end of your sixth chance,if you are unable to guess the number correctly "
"the computer will tell you the correct number goodluck!!!." )


import random

guesses = 6
number = random.randint(1, 50)
win = False

while guesses >0:
    guess = int(input("Guess: "))

    guesses -=1

    if guess > number:
        print("your guess wass too high,you have", guesses, " guess remaining")
    elif guess < number:
        print("your guess wass too low,you have", guesses, "remaining")
    else:
        print("congrats",player, "you guessed the correct number,and won the game!")
        win=True
        guesses=0



if win == False:
    print("sorry", player,"you lose. The number was", number)


    

