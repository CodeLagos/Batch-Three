import random
import sys
def random_inputted_no():
    x=random.randint(1,100)
    count=1
    print(count,"guess(es)")
    y=int(input("Enter any number of your choice between 1 and 100: "))
    if type(y) != int:
        print("Not a number")
    while y!=x:
        if count==6:
            print("You have used all ur guesses")
            sys.exit(0)
        if y > 100:
            print("Numbers between 1 and 100 please")
            sys.exit(0)
        elif y > x:
            print(y,"is too high")
        else:
            print(y,"is too low")
        count+=1
        print(count,"guess(es)")
        y=int(input("Enter any number of your choice between 1 and 100: "))
    if y == x:
        print(y,"is correct, you guessed right")
random_inputted_no()


