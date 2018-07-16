"""     EXAMINATION REGISTRATION APP BY OKPE CHINWENDU EMMANUEL
                PHONE NUMBER: 09068879687
                EMAIL : ECHINWENDU116@GMAIL.COM
                CLASS : CODE LAGOS PYTHON BATCH3,CLASS1
                INSTRUCTORS NAME : MR CHIBOGWU EMMANUEL & MR OYEDELE RIDWAN
    THIS LINES OF CODES HELPS USER REGISTER FOR AN EXAM OF THEIR CHOICE,
          BY ACCEPTING INPUT FROM THE USER,
                 SAVE THEM AND BRINGS THEM OUT WHEN REQUESTED FOR BY THE USER VIA THEIR SURNAME  """            

import random

examination = {1:"programming exam",2:"microsoft exam",3:"dell exam",4:"cisco exam"}
exam_type = ["TYPE1","TYPE2","TYPE3","TYPE4"]
exam_location = ["AGO PALACE WAY","ISOLO","AJAO ESTATE","ILASAMAJA"]
exam_center = ["GRANDMATE COLLEGE","TADEL COLLEGE","FLEEK GATES COLLEGE","SPRING BOARD COLLEGE"]

data={}
def sign_up():
        surname=input("Surname:")
        first_name=input("First name:")
        middle_name=input("Middle name:")
        email=input("Email:")
        age=int(input("Age:"))
        sex=input("Sex:")
        print("TYPE1","TYPE2","TYPE3","TYPE4")
        select=input("Enter your exam type :")  
        if (select.lower() == "type1"):
                exam_type =examination[1]
        elif (select.lower() == "type2" ):
                exam_type = examination[2]
        elif (select.lower() == "type3"):
                exam_type = examination[3]
        elif (select.lower() == "type3"):
                exam_type = examination[4]
        else:
                 print("incorrect type,pls enter a correct type")
        print("registration successful")
        data[surname] = surname,first_name,middle_name,email,age,sex,select
        
       
def examination_details():
    names =input("enter Surname :")
    names = names.lower()
    user_data = data[names]
    det0 = user_data[0]
    print ("SURNAME :",det0)
    det1 = user_data[1]
    print ("FIRST NAME :",det1) 
    det11 =user_data[2]
    print("MIDDLE NAME :",det11)
    det2 =user_data[3]
    print ("EMAIL :",det2)
    det3 =user_data[4] 
    print ("AGE :",det3)
    det4 =user_data[5]
    print ("SEX :",det4)
    det5 =user_data[6]
    print("EXAM TYPE:",det5) 
    registration_no = random.randint(10000000,999999999)
    print ("EXAMINATION NO:",registration_no)
    seat_no = random.randint(100,777)
    print ("SEAT NO :",seat_no)
    exam_location = ["AGO PALACE WAY","ISOLO","AJAO ESTATE","ILASAMAJA"]
    location = random.choice(exam_location)
    print("EXAMINATION LOCATION :",location )
    exam_center = ["GRANDMATE COLLEG","TADEL COLLEGE","FLEEK GATES COLLEGE","SPRING BOARD COLLEGE"]
    center =random.choice(exam_center)
    print("EXAMINATION CENTER :",center)
    print("GOODLUCK")
               
        
while (True):
        print ("""
            WELCOME TO EMMANUEL EXAM.NET
                (WE ARE MADE SO YOU CAN BE MADE)

    WE REGISTER YOU FOR CERTAIN PROFOUND AND PROLIFIC EXAMINATIONS.
    KINDLY BE INFORMED THAT OUR EXAMS ARE REGISTERED BASED ON TYPES.
         TYPE1 EXAM = PROGRAMMING EXAM
         TYPE2 EXAM = MICROSOFT EXAM
         TYPE3 EXAM = DELL EXAM
         TYPE4 EXAM = CISCO EXAM

    PLS KINDLY INDICATE YOUR EXAM TYPE IN ITS REQUESTED SESSION RESPECTIVELY.

    OUR EXAMINATION LOCATIONS & CENTERS ARE SPREAD ACROSS LAGOS NIGERIA ONLY
                                    AND WITH TIME WE INTEND TO SPREAD OUR CENTERS ACROSS ALL BOARDERS OF THE COUNTRY.
                                    
            EXAM LOCATIONS :\n \tAGO PALACE WAY\n \tISOLO \n \tAJAO ESTATE \n \tILASAMAJA
            EXAM CENTERS :\n \tGRANDMATE COLLEGE\n \tTADEL COLLEGE\n \tFLEEK GATES COLLEGE\n \tSPRING BOARD COLLEGE 

     

     AFTER YOUR REGISTRATION,REVIEW YOUR EXAM DETAILS TO SEE YOUR
                                                     EXAMINATION NO,EXAMINATION LOCATION,EXAMINATION CENTER AND SEAT NO.

             NOTE: YOU HAVE TO REGISTER FIRST BEFORE CHECKING FOR YOUR EXAM DETAILS
                             REMEMBER WE ARE MADE SO YOU CAN BE MADE.""")
    

        print("1. \t Register for an exam\n2.\tRequest for exam details\n")
        print("\t PLEASE REGISTER FIRST \n")
        response = input ("enter response\n")
        if (response=="1"):
                sign_up()
        elif (response=="2"):
                examination_details()
        else:
                print("invalid response")
        ext=input("do you want to perform another process?.\t y/n ")
        if(ext.upper()=="N"):
                break
                

