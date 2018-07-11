#a program for data input (form)

print("Fill in your data for registration")
print("Press 1 to start or 2 to exit")
choice1= int(input())
fullname, soo, dob, lga = " ", " ", " ", " "
    
while choice1==1:
    try:
        passage = True
        while passage:
            print("Enter your full-name")
            fullname= int(input())
            if type (fullname) == int:
                print("You have made an invalid entry")
    except:
        print(fullname)
        passage = False
        pass
    
    try:
        passage = True
        while passage:
            print("Enter state of origin")
            soo=int(input())
            if type (soo) == int:
                print("You have made an invalid entry")
    except:
        print(soo)
        passage = False
        pass

    try:
        passage = True
        while passage:
            print("Enter your date of birth")
            dob=int(input())
            if type(dob) == int:
                print(dob)
                passage = False
            
                
    except:
        print("You have made an invalid entry")
        passage = False
        pass
        

    try:
        passage = True
        while passage:
            print ("Enter your Local government Area")
            lga= int(input())
            if type (lga) == int:
                print("You have made an invalid entry")
    except:
        print(lga)
        passage = False
        pass
    

    print(fullname, soo, dob, lga)
    
    print("Your information are the following: ")

    print ("press 2 to start all over again or 3 to exit")
       
    choice2=int(input())
    if choice2==2: continue
    choice3=int(input())
    if choice3==3: break
