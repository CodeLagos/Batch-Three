print("This software is written by Owolagbon Oluwaseun Emmanuel ")
print(" ==========================================================================================================================================")

print(" This is a simple Calculator to solve Simultaneous equations and Quadratic equation. ")
print("                                                                                                                                                                                                                                                               ")
print(" For you information, if you want to solve simultaneous equations type in Simultaneous  and if it's Quadratic equation type in Quadratic")
print(" ==========================================================================================================================================")

User_input = input("Type in the equation using the format above ")

# the first if condition for simultaneous equations

if User_input == "Simultaneous" :
    A1 = int( input(" Enter the coefficient of x in the first equation ") )
    B1 = int( input(" Enter the coefficient of y in the first equation ") )
    C1 = int( input(" Enter the constant in the first equation ") )
    print(" ==========================================================================================================================================")
    A2 = int( input(" Enter the coefficient of x in the second equation ") )
    B2 = int( input(" Enter the coefficient of y in the second equation ") )
    C2 = int( input(" Enter the constant in the second equation ") )
    print(" ==========================================================================================================================================")

    y = float( ( (A1 * C2)  - (A2 * C1) ) / ( ( A1 * B2)  - (A2 * B1))  )
    x = float( ( ( C1) - (B1 * y))  / A1) 
    print ( " the result of the simultaneous equation, x is ",  x , " and y is " , y)
    print(" ==========================================================================================================================================")

# This portion contains the code for the quadratic equation 

elif User_input == "Quadratic" :
    a = int( input("Enter the coefficient of x square") )
    b = int( input(" Enter the coefficient of x ") )
    c = int( input(" Enter the constant of the quadratic equation ") )
    
    x1 = float( ( (-b)  + ( (b**2) - (4 * a * c)) **0.5 ) / 2 * a) 
    x2 = float( ( (-b)  - ( (b**2) - (4 * a * c)) **0.5 ) / 2 * a) 
    print(" The roots of the quadratic equation is ", x1, " and ", x2) 
else:
    print(" Check your input properly for mispelt or inappropriate operation  ")
