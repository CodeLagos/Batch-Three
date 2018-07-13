import random
def randomization():
    print ("Welcome to Mich Randomization of Values")
    print ("Select the below option")
    print ("1- Randomization")
    foption = int(input("Select Option"))
    if (foption == 1):
        print ("Input 1- To Randomize Alphabets \n Input 2- To Randomize Number \n")
        rand_opt = int(input("Select Option"))
        if (rand_opt == 1):
            print ("Select Number of Avaliable Digit")
            print ("1- 3 digit \n2- 4 digit \n3- 5 digit \n4- 6 digit \n5- 7digit \n6- 8 digit ")
            digit = int(input("Enter Digit from available option\n"))
            num = int(input("Number of times\n"))
            if (digit == 1):
                    for i in range(num):
                        i = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
                        j = random.choice(i)
                        k = random.choice(i)
                        l = random.choice(i)
                        print (j + k + l)
            elif (digit == 2):
                for i in range(num):
                    i = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
                    j = random.choice(i)
                    k = random.choice(i)
                    l = random.choice(i)
                    m = random.choice(i)
                    print (j + k + l + m)
            elif (digit == 3):
                for i in range(num):
                    i = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
                    j = random.choice(i)
                    k = random.choice(i)
                    l = random.choice(i)
                    m = random.choice(i)
                    n = random.choice(i)
                    print (j + k + l + m + n)
            elif (digit == 4):
                for i in range(num):
                    i = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
                    j = random.choice(i)
                    k = random.choice(i)
                    l = random.choice(i)
                    m = random.choice(i)
                    n = random.choice(i)
                    o = random.choice(i)
                    print (j + k + l + m + n + o)
            elif (digit == 5):
                for i in range(num):
                    i = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
                    j = random.choice(i)
                    k = random.choice(i)
                    l = random.choice(i)
                    m = random.choice(i)
                    n = random.choice(i)
                    o = random.choice(i)
                    p = random.choice(i)
                    print (j + k + l + m + n + o + p)
            elif (digit == 6):
                for i in range(num):
                    i = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
                    j = random.choice(i)
                    k = random.choice(i)
                    l = random.choice(i)
                    m = random.choice(i)
                    n = random.choice(i)
                    o = random.choice(i)
                    p = random.choice(i)
                    q = random.choice(i)
                    print (j + k + l + m + n + o + p + q)
            else:
                    print ("Input correct number\n")
    if (rand_opt == 2):
        print ("Select Number of Avaliable Digit")
        print ("1- 3 digit \n 2- 4 digit \n 3- 5 digit \n 4- 6 digit \n 4- 7digit \n 6- 8 digit ")
        digit = int(input("Input Digit"))
        num = int(input("number of times Randomization"))
        if (digit == 1):
            for rand in range(num):
                rand = random.randint(100,999)
                print (rand)
        elif (digit == 2):
            for rand in range(num):
                rand = random.randint(1000,9999)
                print(rand)
        elif (digit == 3):
            for rand in range(num):
                rand = random.randint(10000,99999)
                print (rand)
                break
        elif (digit == 4):
            for rand in range(num):
                rand = random.randint(100000,999999)
                print (rand)
        elif (digit == 5):
            for rand in range(num):
                rand = random.randint(1000000,9999999)
                print (rand)
        elif (digit == 6):
            for rand in range(num):
                rand = random.randint(1000000,9999999)
                print (rand)
        else:
            print ("Please Select the Objection")
    else:
        print ("Insert Correct Value ")

randomization()
print ("Do you what to perform another Randomization? Y for yes or N for no \n")
obj = input("Y/N")
obj =obj.upper()
while (obj == "Y"):
    randomization()
else:
    print ("\nBye")