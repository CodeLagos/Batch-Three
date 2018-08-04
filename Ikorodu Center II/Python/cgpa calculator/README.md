# cgpa-calculator

This is a cgpa calculator that requests for students details which includes the student's name, department, level,
total number of courses registered for the semester or session.

The script uses the number of courses registered to determine how many times the for in loop will run.

It then requests for the course details input from the user- the course name, unit weight, and the score obtained 
in each course. It uses the data obtained to calculate the weighted grade point average which is the product of the grade point
and the unit weight. 

The script uses a conditional statement to assign the gradepoint based on the score obtained from the user as input.


The assignGradePoint function does this. The script then appends the course details to a course list which would contain the details of the
courses entered by the user. The script calls the calculateWeightedGradePoint function to calculate the weighted grade point taking the 
grade point, no of units of the course, and the initialised weighted grade point as arguments which then returns the calculated weighted grade point. 

The script then calculates the cumulative grade point average and prints the student records to the screen as well as the courses registered
and the score as well as unit for each course. The script uses a round function to format the cgpa to 1 decimal place.

The script presently calculates the cgpa for a scale of 5.0 but coule be modified to suit the needs of the user.
