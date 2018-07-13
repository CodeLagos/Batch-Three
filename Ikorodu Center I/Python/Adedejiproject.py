#Get user operational input
print("welcome to our improved calculator")
print("For multiplication input'*',For addition input'+',For division input'/',For Subtraction input'-',")
print("========================================================================================")
user_input= input("what mathematical operation will you like to run:")

#First Conditional Statement for multiplication
if user_input == '*':
    firstnumber = float(input("Enter your first number:"))
    secondnumber = float(input("Enter your second number:"))
#This is where the logic happens
    multiple_number= firstnumber*secondnumber
    print("The multiple of",'first_number', "and", 'second_number', "=",multiple_number)

#Second Conditional Statement for Addition
elif user_input == '+':
    print("Good you have choosen the Addition operation")
    print("==============================================")
    first_number = float(input("Enter your first number:"))
    print("==================================================")
    second_number = float(input("Enter your second number:"))
#This is where the logic happens
    addition_number=first_number + second_number
    print("======================================")
    print("The additional of",'first_number', "and", 'second_number' "=",addition_number)

#Third Conditional Statement for Division
if user_input == '/':
    firstnumber = float (input("Enter your first number:"))
    secondnumber = float(input("Enter your second number:"))
#This is where the logic happens
    divid_number= firstnumber/secondnumber
    print("The divisoin of",'first_number', "and", 'second_number', "=",divid_number)                               

#Fourth Conditional Statement for subtraction                                                                     
elif user_input == '-':
    print("Good you have choosen the Subtraction operation")
    print("=================================================")
    first_number = float(input("Enter your first number:"))
    print("======================================================")
    second_number = float(input("Enter your second number:"))
#This is where the logic happens
    subtraction_number=first_number - second_number
    print("=========================================")
    print("The subtraction of",'first number', "and", 'second_number', "=",subtraction_number)
#if there is an invalid......
else:
    print("this is way too much oga")
    
