import random
randomNumber=random.randint(1,10)
values = list(range(40))
random.choice(values)
print("random number has been generated")
guesses=False
while guesses==False:
    userInput=int(input("your guess please:"))
    if userInput==randomNumber:
        guesses=True
        print("congratulation well done:")
    elif userInput > 10:
        print("your guess is higher than number")
    elif userInput < 1:
        print("your guess is lower than number")
    elif userInput > randomNumber:
        print("just one more try or go a bit lower")
    elif userInput < randomNumber:
        print("just one more try or go a bit hihger")
    else :
        print("game over")
