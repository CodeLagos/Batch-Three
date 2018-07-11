# dice game

print ("This is a Game of Dice to be played by two persons")
print ("Coded by Abdulfatah Babatunde")

import random
while True:
    start = input("enter s to start and any other key to exit: ")
    if start == "s" or start == "S":
        Roll = input("player1 press Y to roll a dice: ")
    
        if Roll == "y" or Roll == "Y":
            a = (random.randint(1,6))
            b = (random.randint(1,6))
            c = (random.randint(1,6))
            print("rolling dice........")
            print("rolling dice........")
            print("the values are......")
            print(a)
            print(b)
            print(c)

        else:
            print("ERROR")
            exit()
        Roll = input("player2 press x to roll a dice: ")
        if Roll == "x" or Roll == "X":
            d = (random.randint(1,6))
            e = (random.randint(1,6))
            f = (random.randint(1,6))
            print("rolling dice........")
            print("rolling dice........")
            print("the values are......")
            print(d)
            print(e)
            print(f)
        else:
            print("error")
            exit()

            print("player1 scores equals", a+b+c)
            print("player2 scores equals", d+e+f)
        if a+b+c > d+e+f:
            print("player1 wins")
        elif d+e+f > a+b+c:
            print("player2 wins")
        else:
            print("draw")
    else:
        break
