#this is a short code that helps to calculate users body mass index and tell the category de belong to
while True:
        print ('welcome user kindly follow the prompt  ')
        newuser=input("press 1 to input your data or press 2 to quit: ")
        if newuser =="2":
                print ("goodbye!!!")
                break
        elif newuser=="1":
                print("welcome!!!, please input your data")
        print('======================================================================================')
        name=(input('Name:  ' ))
        age= eval(input ('age:  '))
        height=eval( input ('height:  '))
        weight= eval(input ('weight:  '))
        print('=======================================================================================')
        BMI=(weight*height/age)
        print('your BMI is:  ', BMI,  sep=' ')
        print('=======================================================================================')
        if BMI >=30:
            print('Dear',name, 'according to the world health organization Body mass Index chart,','it is advisable you please watch your weight because you are obess')
        elif BMI <= 18:
            print('Dear',name, 'according to the world health organization Body mass Index chart,','it is advisable you please improve your nutrion because you are underweighed')
        else:
            print('Dear',name, ',''Congratulation!!! you are healthy.')
        
