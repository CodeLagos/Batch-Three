#Get user operational input
print("welcome to my improved calculator")
print("For multiplication input'*',For additional input'+',For division input'/',For Subtraction input'-',")
print("=================================== my name is Sarah =============================================")
user_input= input("What mathematical operation will you like to run: ")                                                       


#First Conditional Statement for multiplication
if user_input == '*':
     firstnumber = float(input("input your first number:"))
     secondnumber= float(input("input your second number:"))
#This is where the logic happens
     multiple_number= firstnumber*secondnumber
     print("==============================")
     print("The multiple of",'firstnumber', "and", 'second_number', "=",multiple_number)
     
#Second Conditional Statement for Addition
elif user_input == '+':
     print("Good you have choosen the Addition Operation")
     print("============================================")
     first_number = float(input("input your first number:"))
     print("=============================================")
     second_number = float(input("input your second number:"))
#This is where the logic happens
     addition_number= first_number + second_number
     print("=======================================")
     print("The additional of", 'first_number', "and", 'second_number', "=",addition_number)
     
#Third Conditional Statement for Division
elif user_input == '/':
     print("Good you have choosen the Division Operation")
     print("============================================")
     first_number = float(input("input your first number:"))
     print("=============================================")
     second_number = float(input("input your second number:"))
#This is where the logic happens
     Division_number= first_number / second_number
     print("=======================================")
     print("The Division of", 'first_number', "and", 'second_number', "=",Division_number)
     
#Fourth Conditional Statement for Subtraction
elif user_input == '-':
     print("Good you have choosen the subtraction Operation")
     print("============================================")
     first_number = float(input("Input your first number:"))
     print("=============================================")
     second_number = float(input("Input your second number:"))
#This is where the logic happens
     Subtraction_number= first_number - second_number
     print("=======================================")
     print("The deduction of", 'first_number', "and", 'second_number', "=",Subtraction_number)
     
#if there is an invalid.....
else:
     print("you are lost")

     
print ("=============================Area Calculation=============================")

#Get user operational input

print("welcome to Enny calculator")

print("For Area of Triangle(AOT) input'1/2*base*height',For Area of Rectangle(AOR) input'length*breadth', For Area of Circle(AOC) input'22/7*radius*height',")

print("================================================================================")
user_input= input("What mathematical operation will you like to run: ")                  
#first Statement for AOT
if user_input == '1/2*base*height':
     print("Good you have choosen the AOT Operation")
     print("============================================")
     Base = int(input("Input the base:"))
     print("=============================================")
     Height = int(input("Input the height:"))
#This is where the logic happens
     AOT= 1/2*Base*Height
     print("=======================================")
     print("The area of Triangle is", '1/2', "and" 'base', "and", 'height', "=",AOT)
     
#Second Statement for AOR
elif user_input == 'length*breadth':
     print("Good you have choosen the AOR Operation")
     print("============================================")
     Length = int(input("Input the Length:"))
     print("=============================================")
     Breadth = int(input("Input the breadth:"))
#This is where the logic happens
     AOR= Length*Breadth
     print("=======================================")
     print("The area of Rectangle is", 'Length', "and", 'Breadth', "=",AOR)
     
#Fourth Statement for AOC
elif user_input == '22/7*radius*height':
     print("Good you have choosen the AOC Operation")
     print("============================================")
     Radius = int(input("Input the radius:"))
     print("=============================================")
     Height = int(input("Input the height:"))
#This is where the logic happens
     AOC= 22/7*Radius*Height
     print("=======================================")
     print("The area of Circle is", 'radius', "and", 'height', "=",AOC)
     #if there is an invalid.....
else:
     print("Invalid code")

