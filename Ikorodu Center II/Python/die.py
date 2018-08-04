#Name: Comfort O. B. Abe
#Project submitted at the completion of code lagos program
#Project supervisor: Rex Ben

from random import randint
print("Welcome to die rolling game. To play you'll have to pick a number between 1 and 6")
while True:
    user = int(input("Roll a die"))
    ran = randint(1,6)
    if(user > 7):
        print("Enter a number between 1 and 6")
    elif(user < 1):
        print("Enter a number between 1 and 6")
    else:
        if(user == ran):
            print("You are a genius. The die number is " + ran)
        else:
            print("Oops, please try again. The die number is " + ran)
