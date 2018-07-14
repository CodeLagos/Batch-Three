"""
This App creates a  CodeLagos Alumni Directory to register and maintain member professional details
Written by Lawal SALMAN, Python class partcipant
Version 1.3 July 12, 2018.  
"""
#
# Initializing the code by defining functions 
import random
CodeLag = {}
class Alumni:
    def __init__(self,name,email,qualifications,jobd):
       self.name=name
       self.email=email
       self.qualifications=qualifications
       self.jobd=jobd
       self.registration_no =random.randint(1000,9999)
    def update(self,award,):
         self.qualifications+=award
    def AccountDetails(self):
        return self.registration_no,self.name,self.email,self.qualifications,self.jobd
    def changeName(self,name):
        self.name=name
        
def CreateAccount():
    name = input("Enter Full Name, surname first in CAPS\n")
    qualifications =input("Enter qualifications, eg: BSc, PhD, PMP,\n")
    email= input("email address?: ")
    jobd = input("Occupation? eg: Engineering  ")
    a1 = Alumni(name,email,qualifications,jobd)
    CodeLag[a1.registration_no] = a1
    print("Account Created Successfully!!\n Your Registration Number is {}".format(a1.registration_no))
    
def update(id,qualifications):
    return CodeLag[id].update(qualifications)

def AccountDetails(id):
    return CodeLag[id].AccountDetails()
   
def changeName(id,name):
    return CodeLag[id].changeName(name)
    
while(True):
#
# Menu Page
    print("\tWelcome to CodeLag Alumni Directory\n Please select a menu item")
    print(" 1.Create Account\n 2.Update Qualifications\n 3.Display AccountDetails\n 4.Change Name")
    
    response = input("Enter Response\n")

    if(response=='1'):
#
# Test of eligibiity for membership
              atnds= int(input("number of CodeLag classes attended?:  "))
              pjct= input("Project completed?, Y/N:  ")
              if(atnds>9 and pjct.upper()== 'Y'):    
               CreateAccount()
              else:
                  print("sorry you are ineligible for registration")
                 
    elif(response=='2'):
        ID =int(input("Enter Your Registration Number"))
        qualifications = input("Enter Your new awards")
        update(ID,qualifications)
        print("Update Succesful")

    elif(response=='3'):
        ID = int(input("Enter Your Registration Number"))
        print(AccountDetails(ID))

    elif(response=='4'):
        ID = int(input("Enter Your Registration Number: "))
        name =input("Enter your new name")
        changeName(ID,name)
        print("Name changed Succesfully!!")
    ext=input("Do you want to carryout another operation?.\t Y/N: ")
    
    if(ext.upper()=='N'):
        print("Have a great day.\n")

        break
