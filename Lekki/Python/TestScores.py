# This script will calculate the average of three test score by Adisa Babatunde

print ("This script will calculate the average of three test score")

# Get three test score
mode = True
while mode:
    try:
        Test1 = int(input("Enter score for test 1: "))
        if type(Test1)== int:
            pass
    
        Test2 = int(input("Enter score for test 2: "))
        if type(Test2)== int:
            pass
        Test3 = int(input("Enter score for test 3: "))
        if type(Test3)== int:
            pass
        mode = False
    except ValueError as e:
        print("You have made an invalid input", e)
        mode  = True
   
# Calculate the average
average = (Test1 + Test2 + Test3) / 3

# Print out the test score
print ("the average test score is: ", average) 
