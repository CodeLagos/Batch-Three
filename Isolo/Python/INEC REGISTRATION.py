""" PROGRAM TITLE: INEC Registration.
NAME: OFUNWA CHIOMA ELIZABETH

NAME OF FACILITATOR: Mr Emmanuel Chibuogu

INEC Registration is a program written after a comprenhensive CodeLagos Python Tutorial organised by the Lagos State Government.

FUNCTIONALITY OF PROGRAM:
-Get the information of potential voters
-Calculate the Age and check for the eligibility of the applicant,
- Assign a unique Verification Identification Number(VIN)
-save the data of the Applicant such that it can be accessed when required by using the unique VIN
"""
print("FEDERAL REPUBLIC OF NIGERIA\nINDEPENDENT NATIONAL ELECTORAL COMMISSION\nVOTER'S CARD")
from datetime import datetime
now= datetime.now()
import datetime

import random
DATA= {}
def voter_data():
      title= input("Title(mr/mrs/master/miss):\t")
      surname= input('surname:\t')
      firstname= input('firstname:\t')
      othername=input('middlename:\t')
      address= input('Address:\t')
      sex= input('Gender:\t')
      phoneNo= input('Phone:\t')
      citizenship= input('Nationality:\t')
      state= input("State of Origin:\t")
      occupation= input('Occupation:\t')
      
      validinput= False
      while not validinput:
            try:
                  year=int(input('enter birth year:'))
                  month= int(input('enter birth month(For example,3=march):'))
                  day= int(input('enter birth day:'))
                  validinput=True
            except:
                  print("please Enter number for your birth month,day and year")
      MONTH= str(month)
      DAY= str(day)
      YEAR= str(year)
      birthday= (MONTH + '/' + DAY + '/' + YEAR)
      DOB=datetime.datetime(year,month,day)
      age=(datetime.datetime.now()-DOB)
      convertdays= int(age.days)
      ageyears= convertdays/365
      Age= int(ageyears)
      if(Age>=18):
            pass
      else:
        print('YOU ARE NOT UP TO AGE FOR THE CARD\nPLS TRY AGAIN WHEN YOU ARE 18YEARS')
      DATA[phoneNo]=surname,firstname,othername,address,sex,birthday,Age,phoneNo,citizenship,state,occupation
def vin():
      num=str(random.randint(100000000000,999999999999))
      a=[chr(i) for i in range(65,123) if chr(i).isalpha()]
      a=random.sample(a,4)
      a=''.join(a)
      no= a+num
      return no
VIN= vin()
def database():
      user= input("Enter your PhoneNo: ")
      print("---------------------------------------------------------------------------")
      theme= '{:^40}'.format('FEDERAL REPUBLIC OF NIGERIA')
      print(theme)
      inec= '{:^30}'.format('INDEPENDENT NATIONAL ELECTORAL COMMISSION')
      print(inec)
      card='{:^50}'.format("VOTER'S CARD")
      print(card)
      date='{:>50}'.format('DATE OF ISSUE:')
      print(date,now)
      user_data=DATA[user]
      det0= user_data[0]
      print ("SURNAME:",det0)
      det1= user_data[1]
      print ("FIRSTNAME:",det1)
      det2= user_data[2]
      print ("OTHERNAME:",det2)
      det3= user_data[3]
      print ("ADDRESS:",det3)
      det4= user_data[4]
      print ("SEX:",det4)
      det5= user_data[5]
      print ("DATE OF BIRTH:",det5)
      det6= user_data[6]
      print ("AGE:",det6)
      det9= user_data[9]
      print ("OCCUPATION:",det9)
      print("VERIFICATION IDENTIFICATION NO.:",VIN)
      print ("--------------------------------------------------------------------------------")

while True:
      voter_data()
      ext= input("Do you want to continue?Y/N:")
      if (ext.upper()=='N'):
            database()
            break
      
