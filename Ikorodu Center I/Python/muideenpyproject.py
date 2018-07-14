print ("Welcome to DEEN Improved Calculator......................")

print ("===========================================================================================================")
print ("===========================================================================================================")

# Explain how it works or functions................. user friendly
print ("For addition input '+', For subtraction input '-', For division input '/', For multiplication input '*', For the raise of power input '**', For floor division input '//'")

# Prompt user to input desired function
user_input = input ("Please input your desired fx: ")

# First logic for Addition
if user_input =="+":
    print ("You intend an addition function...............................")
    print ("Submission confirmed..... you intend an addition fx")
    # Prompt user to input first and second digit
    first_digit = float (input ("Please input your first_digit: "))
    second_digit = float (input ("Please input your second_digit: "))
    addition_fx = first_digit + second_digit
    print ("The sum is: ", first_digit, "and", second_digit, "=", (first_digit + second_digit))
    print ("===========================================================================================================")
    print ("===========================================================================================================")

# Second Logic for Subtraction
elif user_input =="-":
       print ("You intend an subtraction function..........................")
       print ("Submission confirmed..... you intend an subtraction fx")
       # Prompt user to input first and second digit
       first_digit = float (input ("Please input your first_digit: "))
       second_digit = float (input ("Please input your second_digit: "))
       subtraction_fx = first_digit - second_digit
       print ("The difference is: ", first_digit, "and", second_digit, "=", (first_digit - second_digit))
       print ("===========================================================================================================")
       print ("===========================================================================================================")       

# Third Logic for multiplication
elif user_input == "*" or user_input == "multiplication":
       print ("You intend a Multiplication function.....................")
       first_digit = float (input ("Please input your first_digit: "))
       second_digit = float (input ("Please input your second_digit: "))
       multiple_number = first_digit * second_digit
       print ("The Multiple is: ", first_digit, "and", second_digit, "=", (first_digit * second_digit))
       print ("===========================================================================================================")
       print ("===========================================================================================================")    

# Fourth Logic for division
elif user_input == "/":
       print ("You intend a division function.................................")
       first_digit = float (input ("Please input your first_digit: "))
       second_digit = float (input ("Please input your second_digit: "))
       division_number = first_digit / second_digit
       print ("The Division is: ", first_digit, "and", second_digit, "=", (first_digit / second_digit))
       print ("===========================================================================================================")
       print ("===========================================================================================================")

# Fifth Logic for the raise to power of two
elif user_input == "**":
    first_number = float (input ("Enter your first value: "))
    second_number = float (input ("Enter your second value: "))
    raise_power= first_number ** 2
    raise_power1 = second_number **2
    print (raise_power)
    print (raise_power1)
    print ("===========================================================================================================")
    print ("===========================================================================================================")

# Sixth Logic for floor division
elif user_input == "//":
    first_number = float (input ("Enter your first value: "))
    second_number = float (input ("Enter your second value: "))
    square_root = first_number //2
    print (square_root)
    print ("===========================================================================================================")
    print ("===========================================================================================================")

# Incase of an invalid input the else statement runs
else:
    print ("Invalid Input, Please Try Again!!!!!")
    print ("Thank you for using our Improved Calculator.................................................")
    print ("===========================================================================================================")
    print ("===========================================================================================================")
