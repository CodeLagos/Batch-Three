# This is a guess game.
import random #The second line is an import statement,statements are instructions that perform some action but don’t evaluate to a value like expressions do. i imported the module named random so that the program can call random.randint(). This function will come up with a random number for the user to guess.
import time

startingtime = time.time()
guesses = 0 # store the number of guesses the player has made in this variable. Since the player hasn’t made any guesses at this point in the program,  i stored the integer 0 here.
print('Hello! What is your name?') #asking for user's name to make it look fun using the print function.
myName = input()#lets the user type in their name and stores it in the myName variable.
number = random.randint(1, 100)#calling a new function named randint() and stores the return value in number. Remember, function calls can be part of expressions because they evaluate to a value.The randint() function is provided by the random module in line 2.
print('Well, ' + myName + ', I am thinking of a number between 1 and 100.')#the print function is in use again,welcomimg the user and telling the user that the computer is thinking of a random between a range of numbers.

while guesses < 7: #this is a while statement, which indicates the beginning of a while loop. Loops let you execute code over and over again.The < sign is a comparisonoperator.Comparison operators compare two values and evaluate to a True or False Boolean value
    print('Take a guess.')#asking the user to input the secret number he/she thinks is coorect using the print function
    guess = input()#user inputing the number 
    guess = int(guess)#The int() function takes one argument and returns an integer value form of that argument

    guesses = guesses + 1 #Once the user has taken a guess, the number of guesses should be increased by one.
    print(7 - guesses,"guesses left")

    if guess < 0: # this is an if statement. The execution will run the code in the following block if the if statement’s condition evaluates to True. If the condition is False, then the code in the if-block is skipped. checks if the user’s guess is less than the computer’s secret number. If so, then the execution moves inside the if-block on next line and prints a message telling the user this
        print('You are far away,the number is between 1 and 100')
    if guess < number:#checks if the user’s guess is greater than the secret number. If this condition is True, then the print() function call tells the player that their guess is too low.
        print('Your guess is too low,very close.')
    if guess > number:#checks if the user’s guess is greater than the secret number. If this condition is True, then the print() function call tells the user that their guess is too high.
        print('Your guess is too high.')
    if guess == number:#The if statement on this line checks if the guess is equal to the secret number. If it is, the program runs the break statement on the next line.
        break
if guess == number:#checks to see if the user guessed correctly. If so, the execution enters the if-block to the next line.
        guesses = str(guesses)
        print('Good job, ' + myName + '! You guessed my number in ' + guesses + ' guesses!')

if guess != number:#using the “not equal to” comparison operator != to check if user’s last guess is not equal to the secret number. If this condition evaluates to True, the execution moves into the if-block on the next line.
    number = str(number)
    print('Game over, You lost woefully')
    print('Nope. The number I was thinking of was ' + number)
   
endingtime = time.time()
timeused = str(int(endingtime - startingtime))
print("it took you " + timeused + ' seconds')
