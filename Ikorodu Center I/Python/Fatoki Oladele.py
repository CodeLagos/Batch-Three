import random
def computerGenerated():
    global compGen
    compGen = []
    for i in range(6):
        rNum = random.randint(1,99)
        compGen.append(rNum)
def gameInstructions():
    print("""Welcome Player to Baba Ijegba Lottery Game.
This is how to play;
    The computer generates six numbers in a sequence
    You are required to guess the six numbers
This is how the point will be rewarded
    For every correct number guessed, you will be awarded 1 point
    For every correct number at the correct position, you will be awarded 3 point
    For every correct 2 number sequence, you will be awarded 5 points
    for every correct 2 number sequence at the exact position you will be awarded 10 points.
    Your total point will be a cummulative of all the acquired points.
    You get 100 Naira for every point
Hope you enjoy the game!""")
def mainGame():
    print ("Computer has generated 6 numbers, guess the six numbers from 1 to 99")
    global playerGen
    playerGen = []
    j = 1
    while (j < 7):
        pNum = int(input("Enter a number (" + str(j) + "): "))
        if (not (pNum > 0 and pNum < 100)):
            print("You must enter a number from 1 to 99")
            continue
        else:
            playerGen.append(pNum)
            j = j+1
def firstCheck():
    global firstCondition
    global firstPoint
    firstCondition = [c for c in playerGen if c in compGen]
    firstPoint = len(firstCondition)
def secondCheck():
    global secondCondition
    global secondPoint
    k = 0
    secondCondition = 0
    while (k < 6):
        if (playerGen[k] == compGen[k]):
            secondCondition = secondCondition + 1
        k = k + 1
    secondPoint = secondCondition * 3
def thirdCheck():
    global thirdCondition
    global thirdPoint
    global forthCondition
    global forthPoint
    compSeqn = []
    playerSeqn = []
    for i in range(5):
        pSeqn = str(playerGen[i]) + str(playerGen[i + 1])
        cSeqn = str(compGen[i]) + str(compGen[i + 1])
        playerSeqn.append(pSeqn)
        compSeqn.append(cSeqn)
    thirdCondition = [e for e in playerSeqn if e in compSeqn]
    thirdPoint = (len(thirdCondition)) * 5
    forthCondition = 0
    for i in range(5):
        if (compSeqn[i] == playerSeqn[i]):
            forthCondition = forthCondition + 1
    forthPoint = forthCondition * 10
def result():
    firstCheck()
    secondCheck()
    thirdCheck()
    print("Computer generated numbers are; ", compGen)
    print("Your numbers are; ", playerGen)
    print("You had")
    print(firstPoint, "point from", firstPoint, "correct guess(es)")
    print(secondPoint, "point from", secondCondition, "correct position(s)")
    print(thirdPoint, "point from", len(thirdCondition), "correct 2 number sequence")
    print(forthPoint, "point from", forthCondition, "correct 2 number sequence at exact position")
    global totalPoint
    totalPoint = firstPoint + secondPoint + thirdPoint + forthPoint
    print("You have total of", totalPoint ,"point")
    print("You won", (totalPoint*100), "Naira")
def again():
    playAgain = input("Play again?(y/n): ")
    if (playAgain.upper() == "Y"):
        realGame()
    elif (playAgain.upper() == "N"):
        print("Thank you for playing Baba Ijegba. Hope you enjoyed it!")
    else:
        again()

def realGame():
    computerGenerated()
    mainGame()
    result()
    again()
def babaijegba():
    gameInstructions()
    realGame()
babaijegba()
