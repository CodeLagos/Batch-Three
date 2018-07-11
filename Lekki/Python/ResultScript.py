#Code Lagos Python Class 18
#Israel Tobi 

import datetime

#================== FUNCTION DECLARATIONS ==========================

# A function to read data from a text files
def filereader(filename):
    if filename.endswith('.txt'):
        with open(filename, 'r') as f:
            return f.readlines()
    else: raise ValueError("File name must end with .txt")

# A function to write data to a text file
def filewriter(filename, lines):
    with open(filename, 'a+') as f:
        return f.writelines(lines)

# A function to print Student's Name
def getName(fn, ln):
    return fn+" "+ln
#??????
def getCount(score):
    if score > 49 and score <= 100:
        return 1
    elif score > 39 and score < 50:
        return 1
    elif score > 0 and score < 40:
        return 1

# A function to determine score grade and remarks
def getScoreInfo(score):
    if score > 74 and score <= 100:
        return str(score)+"\t  A1\t  Excellent"
    
    elif score > 69 and score < 75:
        return str(score)+"\t  B2\t  Very Good"

    elif score > 64 and score < 70:
        return str(score)+"\t  B3\t  Good"
        
    elif score > 59 and score < 65:
        return str(score)+"\t  C4\t  Credit"
        
    elif score > 54 and score < 60:
        return str(score)+"\t  C5\t  Credit"
        
    elif score > 49 and score < 55:
        return str(score)+"\t  C6\t  Credit"
        
    elif score > 44 and score < 50:
        return str(score)+"\t  D7\t  Pass"
        
    elif score > 39 and score < 45:
        return str(score)+"\t  D8\t  Pass"
        
    elif score > 0 and score < 40:
        return str(score)+"\t  F9\t  Fail"




#=================== MAIN PROGRAM BLOCK ============================

#Variable decalarations
rawFileContents, datafeedArray, studentsScores = [], [], []
runcount, innercount = 0, 0
yr = datetime.datetime.now()
generalRemarks = "\tRemarks: You did Great in {} Courses, Fair in {} Courses and Poor in {} Courses\n\n"
advice = "\n\tNote: Failed and Pass Courses are Advised to be retaken\n\t*******************************************************"
fileHeader = "\t\t\tFINAL EXAMINATION RESULT\n\t\t\t************************\n\t\t\t************************\n"

#Opening the input file
try:
    infile = filereader('rawResult.txt')
except IOError as e:
    print("File could not be opened; ", e)
except ValueError as e:
    print("Unrecognized file name; ", e)

# Reading and storing the file contents to a list (and getting rid of all form of white spaces)
for lines in infile:
    rawFileContents.append(lines.split())

# Creating anoter list to contain Student's details
for data in rawFileContents:
    if data == rawFileContents[0]:
        pass
    else:
        studentsScores.append(data)

# Reading from all the lists and formating the output 
while runcount < len(rawFileContents):
    for row in rawFileContents:
        scoreCounter = 2
        great, passed, failed = 0, 0, 0
        for column in row:
            datafeedArray = studentsScores[runcount]
            if rawFileContents.index(row) == 0 and row.index(column) == 0:
                filewriter(getName(datafeedArray[0], datafeedArray[1])+" Transcript.txt", "\n"+fileHeader+"\n")
                print(fileHeader)
                filewriter(getName(datafeedArray[0], datafeedArray[1])+" Transcript.txt", (column+":\t"+getName(datafeedArray[0], datafeedArray[1])+"\n"))
                print(column, ":\t", getName(datafeedArray[0], datafeedArray[1]))
                filewriter(getName(datafeedArray[0], datafeedArray[1])+" Transcript.txt", ("Session: Final\nYear: {}\n\n".format(yr.year))+"\n")
                print("Session: Final\nYear: {}\n\n".format(yr.year))
                filewriter(getName(datafeedArray[0], datafeedArray[1])+" Transcript.txt", "Subjects\t  Score\t  Grade\t  Remarks\n========\t  =====\t  =====\t  =======\n")
                print("Subjects\t  Score\t  Grade\t  Remarks\n========\t  =====\t  =====\t  =======\n")
                
            else:
                filewriter(getName(datafeedArray[0], datafeedArray[1])+" Transcript.txt", (column+"\t  "+getScoreInfo(int(datafeedArray[scoreCounter])))+"\n")
                print(column, "\t  ", getScoreInfo(int(datafeedArray[scoreCounter])))
                scoreCounter +=1
                        

        filewriter(getName(datafeedArray[0], datafeedArray[1])+" Transcript.txt", advice)        
        print(advice)
        runcount += 1
        break
    if runcount == (len(rawFileContents)-1):
        break
