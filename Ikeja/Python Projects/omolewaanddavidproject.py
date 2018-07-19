#The random Guesser done by Omolewa Joshua and David Michael in Completion of Python Project in Code Lagos

# THE RANDOM GUESSER
print ("Welcome, we hope enjoy The Random Guesser game ")
print()
print("We want to test your guessing skills, 'HAVE FUN' ")
print()
mode=int(input("Choose your level. Enter 1 for Easy, 2 for Medium, 3 for HARD, 4 for LEGENDARY "))
storage=[]

import random
#This variable is used for the number of trials
guess=7

m=0
#This function generate a random number between 1-100
def random2():
    t=random.randint(1,100)
    return t

#This function stores the inputed difficulty level in an array "storage" and returns the last array value (LAST difficulty played
def storage1 (a):
    storage.append(a)
    c=storage[-1]
    return c

#This function takes the number inputed by the user and tells how high or low it is to the genrated and also the level of difficulty
#number

#EASY
def indicator (b,k): 
    if (b - k)<= 15 and (b-k)>=0:
        print ("Your guessed value is High")
        
        if (b - k)<= 5 and (b-k)>=0:
            print("You are very close")
    elif (b-k)>=-15 and (b-k)<0:
        print ("Your guessed number is low")
        if (b-k)>=-5 and (b-k)<0:
            print ("You are very close")
    elif (b-k) <-15:
        print ("your guessed number is too low")
    
    else:
            print ("your guessed number is too High ")
            print()
#MEDIUM
def indicator2 (b,k):
    if (b - k)<= 25 and (b-k)>=0:
        print ("Your guessed value is High")
        
        if (b - k)<= 10 and (b-k)>=0:
            print("You are  close")
    elif (b-k)>=-25 and (b-k)<0:
        print ("Your guessed number is low")
        if (b-k)>=-10 and (b-k)<0:
            print ("You are close")
    else:
        print ("your are far off")

#HARD
def indicator3 (b,k):
    if (b - k)<= 12 and (b-k)>=0:
        print ("Your guessed value is  High")
        
    elif (b-k)>=-12 and (b-k)<0:
        print ("Your guessed number is Low")
        
    else:
        print("You are far off")

#LEGENDARY
def indicator4 (b,k):
    if (b - k)<= 2 and (b-k)>=0:
        print ("Your guessed value is  HIGH")
        
    elif (b-k)>=-2 and (b-k)<0:
        print ("Your guessed number is LOW")
        
    else:
        print("You are far off")


#This Main loops contain the main code for the game and  ask for the user input and loops through the number of guesses until it reaches 0 and stops
#included in the loop is the mode of diffculty
def maincode(guess):
    k=random2()
    y=k
    v= str (k)
    show1 = [ '*' for r in v]
    c = storage1 (mode)
    
    print()
    while guess!=0:
        print()
        
        print()
        print (''.join(show1))
        
        user_input = int (input ("Guess what number  is displayed in '**' from (1-100) "))
        if user_input == y:
            print()
            print ("Congratulations you guessed the number correctly")
            print()
            changelevel()
            
            break
        else:
            guess = guess-1
            if guess!=0 and c==1:
                indicator(user_input,y)
                print ()
                print ("You have ",guess,"attempts left")
            elif guess!=0 and c==2:
                    indicator2(user_input,y)
                    print ()
                    print ("You have ",guess,"attempts left")
            elif guess!=0 and c==3:
                    indicator3(user_input,y)
                    print ()
                    print ("You have ",guess,"attempts left")
            elif guess!=0 and c==4:
                    indicator4(user_input,y)
                    print ()
                    print ("You have ",guess,"attempts left")
                
                    
    if guess==0:
        print()
        print("GAME OVER")
        print()
        print("You have exhausted the number of trials")
        print ()
        print("The actual number is ",y, "Try again")
        print()
        changelevel()
def maincode2(guess):
    k=random2()
    y=k
    v= str (k)
    show1 = [ '*' for r in v]
    l=storage[-1]
    r = storage1 (l)
    
    print()
    while guess!=0:
        print()
        
        print()
        print (''.join(show1))
        
        user_input = int (input ("Guess what number  is displayed in '**' from (1-100) "))
        if user_input == y:
            print()
            print ("Congratulations you guessed the number correctly")
            print()
            changelevel()
            
            break
        else:
            guess = guess-1
            if guess!=0 and l==1:
                indicator(user_input,y)
                print ()
                print ("You have ",guess,"attempts left")
            elif guess!=0 and l==2:
                    indicator2(user_input,y)
                    print ()
                    print ("You have ",guess,"attempts left")
            elif guess!=0 and l==3:
                    indicator3(user_input,y)
                    print ()
                    print ("You have ",guess,"attempts left")
            elif guess!=0 and l==4:
                    indicator4(user_input,y)
                    print ()
                    print ("You have ",guess,"attempts left")
                
                    
    if guess==0:
        print()
        print("GAME OVER")
        print()
        print("You have exhausted the number of trials")
        print ()
        print("The actual number is ",y, "Try again")
        print()
        changelevel()

def maincode3(guess,b):
    k=random2()
    storage.append(b)
    
    y=k
    v= str (k)
    show1 = [ '*' for r in v]
    
    print()
    while guess!=0:
        print()
        
        print()
        print (''.join(show1))
        
        user_input = int (input ("Guess what number  is displayed in '**' from (1-100) "))
        if user_input == y:
            print()
            print ("Congratulations you guessed the number correctly")
            print()
            changelevel()
            
            break
        else:
            guess = guess-1
            if guess!=0 and b==1:
                indicator(user_input,y)
                print ()
                print ("You have ",guess,"attempts left")
            elif guess!=0 and b==2:
                    indicator2(user_input,y)
                    print ()
                    print ("You have ",guess,"attempts left")
            elif guess!=0 and b==3:
                    indicator3(user_input,y)
                    print ()
                    print ("You have ",guess,"attempts left")
            elif guess!=0 and b==4:
                    indicator4(user_input,y)
                    print ()
                    print ("You have ",guess,"attempts left")
                
                    
    if guess==0:
        print()
        print("GAME OVER")
        print()
        print("You have exhausted the number of trials")
        print ()
        print("The actual number is ",y, "Try again")
        print()
        changelevel()

#This function tells the user to continue or end the game

def retry ():
    print()
    tryagain= int(input ("Enter 1 to continue or Enter any key to exit game "))
    if tryagain == 1:
        maincode2(guess)
    else:
        print()
        print ("Thanks for playing we hope you play again, Goodbye")
    
        
#This function gives you the option to change the level at end of the game
def changelevel():
    print()
    changemode=int(input ("Do You want to change the difficulty level. Enter 1 to change , Enter 2 retry or Enter  any key to exit game "))
    print()
    if changemode==1:
        p= int(input("Choose your level. Enter 1 for Easy, 2 for Medium, 3 for HARD, 4 for LEGENDARY "))
        maincode3(guess,p)
    elif changemode==2:
        retry()
        
    else:
        print()
        print ("Thanks for playing we hope you play again, Goodbye")
        

#I called the maincode fuction to start the game
maincode(guess)


    



    

                 



    
    
        
    
        

    

