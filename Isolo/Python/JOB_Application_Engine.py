""" PROJECT TITLE: JOB Application Engine.
NAME: ONYEMAECHI CHINAGOZIM KELECHI

NAME OF FACILITATOR: Mr. Chibuogu Emmanuel

JOB Application Engine is a software framework syntax written after sheer codeLagos python Training organized by the Lagos State Government.

FUNCTIONALITY OF THE SYNTAX:
1. Garners the applicants bioData (of Lagos and Non-Lagos Residents)
2. Rounds up other user information
3. Assigns a unique Application number to all applicants
4. Programmer forwards the applicants Data to their respective dream_jobPlacement positions"""


print("Welcome\t to\t ONYEMAECHI\'S Job Application Engine\n Email_address: chinagoaimK009@yahoo.com\n Account_no: 0141137639(GTBank)")
def applicants_bioData ():
    names = input ("Surname, Firstname, Middlename:\t")
    gender = input ("Male OR Female:\t")
    DOB = input ("Day/Month/Year of birth:\t")
    citizenship = input ("Nationality:\t")
    religion = input ("your Religion:\t")
    marital_Status = input ("Single/Married/Divorced/Seperated:\t")
    email_Address = input ("enter your email_Address:\t")
    print ("Hello {} your email_Address is {}".format(names,email_Address))

def other_userData ():
    credentials = input ("upload your Resume, Transcripts and writingSample via our email_Address")
    rsd = input ("Do you reside in Lagos?.\t Y/N")
    ext = input ("Have you uploaded your credentials?.\t Y/N")
    if (rsd.upper() == 'Y' and ext.upper () == 'Y'):
        print ("Pay application fee [#5,000] & save your Application number")
    else:
        print ("ONLY Lagos State Residents are qualified to apply!!\n")
        ext = input ("Do you wish to continue?.\n Y/N")
        if ext.upper () == 'N':
            print("Thank You for using this Application Portal; Found below is your Application number\n")
        else:
            print("Ignore the Application number & try again in 5 minutes")

import random
app_No = {}
def app_No ():
    for i in range (1):
        i = random.randint (10000, 99999)
        i = str(i)
        alpha = ['A', 'B', 'C', 'D', 'E', 'V', 'W', 'X', 'Y', 'Z']
        n1 = random.choice (alpha)
        n2 = random.choice (alpha)
        print(i+n1+n2)

while (True):

    print("Select options\n")
    print("1. \tMedical Schools\n2. \tResearch Institutes\n3. \tOil Companies\n4. \tLaw Firms\n5. \tIT_Jobs\n")
    response = input("Enter Response\n")
    if response == '1':
        print("A. \tLUTH\nB. \tLASUTH\n")
        ext = input ("Select option; A/B:")
        if (ext.upper () == 'A' or ext.upper () == 'B'):
            applicants_bioData ()
            other_userData ()
            app_No ()
            break
        else:
            print("INCORRECT ENTRY! Retry..\n")
            ext = input ("Do you want to carry out another operation?.\n Y/N")
            if ext.upper () == 'N':
                print("Thank You for using this Application Portal.\n")
                break
    elif response == '2':
        print ("A. \tNIMER\nB. \tFIIRO\nC. \tNIOMRH\n")
        ext = input ("Select option; A/B/C:")
        if (ext.upper () == 'A' or ext.upper () == 'B' or ext.upper () == 'C'):
            applicants_bioData ()
            other_userData ()
            app_No ()
            break
        else:
            print("INCORRECT ENTRY! Retry..\n")
            ext = input ("Do you want to carry out another operation?.\n Y/N")
            if ext.upper () == 'N':
                print("Thank You for using this Application Portal.\n")
                break
    elif response == '3':
        print ("A. \tChevron\nB. \tShell_Petroleum\nC. \tEXXON_Mobil\nD. \tSunTrust_Oil\nE. \tPillar_Oil\n")
        ext = input ("Select option; A/B/C/D/E:")
        if (ext.upper () == 'A' or ext.upper () == 'B' or ext.upper () == 'C' or ext.upper () == 'D' or ext.upper () == 'E'):
            applicants_bioData ()
            other_userData ()
            app_No ()
            break
        else:
            print("INCORRECT ENTRY! Retry..\n")
            ext = input ("Do you want to carry out another operation?.\n Y/N")
            if ext.upper () == 'N':
                print("Thank You for using this Application Portal.\n")
                break
    elif response == '4':
        print ("A. \tAluko&Oyebode\nB. \tLewis_Ogunbiyi\nC. \tLexPrimus\nD. \tLogistix_Solicitors\nE. \tL&A-legalConsultants\n")
        ext = input ("Select option; A/B/C/D/E:")
        if (ext.upper () == 'A' or ext.upper () == 'B' or ext.upper () == 'C' or ext.upper () == 'D' or ext.upper () == 'E'):
            applicants_bioData ()
            other_userData ()
            app_No ()
            break
        else:
            print("INCORRECT ENTRY! Retry..\n")
            ext = input ("Do you want to carry out another operation?.\n Y/N")
            if ext.upper () == 'N':
                print("Thank You for using this Application Portal.\n")
                break
    elif response == '5':
        print ("A. \tsoftware_Developer\nB. \tnetwork_Engineer\nC. \tdatabase_Admin\n")
        ext = input ("Select option; A/B/C:")
        if (ext.upper () == 'A' or ext.upper () == 'B' or ext.upper () == 'C'):
            applicants_bioData ()
            other_userData ()
            app_No ()
            break
        else:
            print("INCORRECT ENTRY! Retry..\n")
            ext = input ("Do you want to carry out another operation?.\n Y/N")
            if ext.upper () == 'N':
                print("Thank You for using this Application Portal.\n")
                break
