print("FEDERAL REPUBLIC OF NIGERIA\nINDEPENDENT NATIONAL ELECTORAL COMMISSION\nVOTER'S CARD")
from datetime import datetime
now= datetime.now()
print('DATE OF ISSUE:',now)
import datetime

import random

print("------PERSONAL iNFORMATION----------------------------------------------------------")
title= input("Mr/Mrs/Ms:\t")
surname= input('surname:\t')
firstname= input('firstname:\t')
othername=input('middlename:\t')
sex= input('Gender:\t')

print("------D.O.B-------------------------------------------------------------------------")
year= int(input('enter birth year: '))
month= input('enter birth month: ')
day= int(input('enter birth day: '))

year1 = 2018 - year
if (year1>=18):
	print("continue")
else:
	print("Try again when you are 18")
print("------LOCALITY----------------------------------------------------------------------")
citizenship= input('Nationality:\t')
SOO= input("State of Origin:\t")
LGC= input("Local Government:\t")

print("------ADDRESS DETAILS-----------------------------------------------------------")
address= input("Residential Address:\t")
LGC= input("Local Government:\t")
SOR= input("State:\t")
country= input("Country:\t")

print("------CONTACT DETAILS----------------------------------------------------------")
phone= input("Phone no:\t")
mail= input("Email Address:\t")

print("--------------------------------------------------------------------------")
print("NOTE: Registering more than once, giving false information in any application for registration as a voter, or unlawful possession of a voter's card, selling or buying of voters card is called an electoral offence.")
print("------------------------------------------------------------------------")
print("Breaches or violation of some of the provisions often attract penalties, which on conviction may be a fine, a term of imprisonment, or both..")

print("------------------------------------------------------------------------")

print("press the enter key to save")

print("your data has been succesfully saved, We will contact you when your card is available for pick up")

##    DOB=datetime.datetime(year,month,day)
##    age=(datetime.datetime.now()-DOB)
##    convertdays= int(age.days)
##    ageyears= convertdays/365
##    Age= int(ageyears)
##    if(Age>=18):
##       print("Age:",Age)
##    else:
##        print('YOU ARE NOT UP TO AGE FOR THE CARD\nPLS TRY AGAIN WHEN YOU ARE 18YEARS')
##def vin():
##      num=str(random.randint(100000000000,999999999999))
##      a=[chr(i) for i in range(65,123) if chr(i).isalpha()]
##      a=random.sample(a,4)
##      a=''.join(a)
##      no= a+num
##      return no
##
##while True:
##      user= voter_data()
##      info= Age()
##      VIN= vin()
##      
