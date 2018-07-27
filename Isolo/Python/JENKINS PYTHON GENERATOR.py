''' Author: Jenkins Ikechukwu Omereonye
    Email:  Justize9@gmail.com
    Phone:  08163068672
    Python 2, Batch 3 Project'''

'''JENKINS PYTHON GENERATOR'''

'''This is a python program that helps generate a strong and secured password by accepting user input and
randomly generating a unique password from the data the user has inputed.
The user have the opportunity to choose the length and number of password'''

import random

print('''
Jenkins Password Generator
==========================
''')

Jenkins = 1
while Jenkins == 1:
  input("\n\npress enter and follow the requirements to generate your strong password")
  
  print("Enter Your First Name_")
  First_Name = input()

  print("Enter Your Last Name_")
  Last_Name = input()

  print("Enter your date of birth_")
  Dob = input()
  
  print("How old are you_")
  Age = input()
  
  print("Enter your email address_")
  Email = input()
  
  print("whats you mobile line_")
  Mobile_no = input()
  
  number = input('Enter the number of passwords :\n')
  number = int(number)

  length = input('Enter the password length :\n')
  length = int(length)


  print('\nHere are your passwords '+ First_Name)

  for pwd in range(number):
    password = ''
    for c in range(length):
      password += random.choice(First_Name + Last_Name + Age + Email + Dob + Mobile_no)
    print(password)
  
  Regenerate = input("Do you want to generate another password?: [Y/N] ")
  if Regenerate.upper == "Y":
    J = 1
  elif Regenerate == "N":
    exit()
  
    
