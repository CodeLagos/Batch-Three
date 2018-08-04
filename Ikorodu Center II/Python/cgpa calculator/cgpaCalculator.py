print("This is a CGPA calculator that requests for student details as well as course details for a semester and calculates the cgpa for the user")

#Obtains student details from user
user_name = input("Kindly enter your name? ")
dept_name = input("Kindly enter your department's name? ")
user_level = (input("Kindly enter your level? "))
no_of_courses = int(input("Kindly enter the number of courses you took for the semester? "))
print("\n")
#initialises variables-course list, weighted grade point and sum of units
courses_list = []
weighted_grade_point = 0
total_units = 0

#function that assigns grade point based on the score and returns the assigned grade point
def assignGradePoint(score):
    if(score >= 70 and score <= 100):
        grade_point = 5

    elif(score >= 60 and score < 70):
        grade_point = 4

    elif(score >= 50 and score < 60):
        grade_point = 3

    elif(score >= 45 and score < 50):
        grade_point = 2

    elif(score < 40 and score < 45):
        grade_point = 1

    else:
        grade_point = 0

    return grade_point

#function that calculates and returns the weighted grade point
def calculateWeightedGradePoint(wgp,gp,no_unit):
    result = wgp +  gp * no_unit
    return result

#function that calculates the total sum of units
def calculateTotalUnits(total_units,no_of_units):
    sum_units = total_units + no_of_units
    return sum_units

#loop that requests for course name , unit weight and score and pushes to the course details list
for i in range(no_of_courses):
    course_name =  str(input("Kindly enter the course name? "))
    no_of_units =  int(input("Kindly enter the number of units? "))
    score =  int(input("Kindly enter your score? "))
    
    course_detail = {"course_name":course_name.upper(),"no_of_units":no_of_units,"score":score}
    courses_list.append(course_detail)

    grade_point = assignGradePoint(score)

    weighted_grade_point = calculateWeightedGradePoint(weighted_grade_point, grade_point, no_of_units)

    total_units = calculateTotalUnits(total_units,no_of_units)
    
    print("\n")
#calculates cumulative grade point average
cgpa = weighted_grade_point/total_units

#Prints Result for User
print("STUDENT TRANSCRIPT FOR ",dept_name.upper())
print("Name of Candidate\t\t",user_name)
print("Level\t\t\t",user_level)
print("No of Courses Registered \t", no_of_courses)
print("\nCourse Name\tNo of Units\tScore")
#prints all the course details within the array
for course in courses_list:
    print(course["course_name"],"\t",course["no_of_units"],"\t\t",course["score"])

cgpa = round(cgpa,1)
print("Total Units",total_units)
print("Your CGPA is ",cgpa)



    
        
