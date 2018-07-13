"""IsoloNG Drivers Lincense App
   CODE LAGOS 3.0
   Name: Olumodeji Elijah Ayodeji
   phone: 08070587878
   email: elijah.ayodeji@yahoo.com
   
Name of Instructor: Mr Emmanuel Chibuogu

IsoloNG Drivers Lincense App was written using python Language after attending CodeLagos Tutorial Organised by  the Lagos state Government

FUNCTIONS of the app:
-Get the data or information of applicants
-Calculate the Age and check for the eligibility of the applicant,
- Assign a unique driver's license number
-Saves the data of successful applicants and can be accessed using their unique drivers license number
"""
import random
from datetime import datetime
import datetime
from datetime import date
user = {}
class D_license:
 	"""docstring for D_license"""
 	def __init__(self, name, location):
 		super(D_license, self).__init__()
 		self.name = name
 		self.location = location
def CreateAccount():
		print ("Create Account\n ********************\n")
		first_name=input("First Name: ")
		first_name = first_name.capitalize()
		last_name=input("Last Name: ")
		last_name = last_name.capitalize()
		name=first_name+" "+last_name      
		phone_no=int(input("Phone Number:"))
		validinput= False
		while not validinput:
			try:
				year=int(input("Enter Year of Birth('e.g' 2018'): "))
				month=input("Enter Month of Birth('e.g. February or 2'): ")
				month=str(month)
				month=month.capitalize()
				if (month=="January" or month=="1"):
					month=1
				elif (month=="February" or month=="2"):
					month=2
				elif (month=="March" or month=="3"):
					month=3
				elif (month=="April" or month=="4"):
					month=4
				elif (month=="May" or month=="5"):
					month=5
				elif (month=="June" or month=="6"):
					month=6
				elif (month=="July" or month=="7"):
					month=7
				elif (month=="August" or month=="8"):
					month=8
				elif (month=="September" or month=="9"):
					month=9
				elif (month=="October" or month=="10"):
					month=10
				elif (month=="November" or month=="11"):
					month=11
				elif (month=="December" or month=="12"):
					month=12
				else:
					return "Invalid month"
				day= int(input("Enter Day of Birth('e.g 11)':"))
				validinput=True
			except:
				print("please Enter number for your birth month,day and year")
			month1= int(month)
			month2=str(month)
			day1= str(day)
			year1= str(year)
			birthday= (day1+"-"+month2+"-"+year1)
			
			dob=datetime.datetime(year,month1,day)
			today=datetime.datetime.now()
			age=(today-dob)
			cdays=int(age.days)
			age= cdays/365
			age1=int(age)
			if(age>=18):
				pass
			else:
				return "you're not Eligible for Registration"
		print("""       \t\t\t\t*********************
				 |    Location		|
				**********************
				1. Abuja
				2. Osun
				3. Kwara
				4. Kaduna
				5. Lagos
				6. Plateau
				************************
				************************
			""")
		state=input("Select Location(using 1.,2.,...,6.):")
		location = {"ABJ": "Abuja","OSU":"Osun","KWR":"Kwara","KAD":"Kaduna","LAG":"Lagos","PLA":"Plateau"}
		if (state=="1"):
			location=location["ABJ"]
		elif(state=="2"):
			location=location["OSU"]		
		elif(state=="3"):
			location=location["KWR"]
		elif(state=="4"):
			location=location["KAD"]
		elif(state=="5"):
			location=location["LAG"]
		elif(state=="6"):
			location=location["PLA"]
		else:
			return "Invalid Location"
		print("""       ---Account Created Successfully!!!---
			Name:{}
			Phone Number:{}
			Birthday:{}
			Age:{}
			Location:{}


			""".format(name,phone_no,birthday,age1,location))
		user[phone_no]=name,phone_no,birthday,age1,location

def license_no():
	phone_no=int(input("Enter Phone Number: "))
	user_phone_no=user[phone_no]
	name=user_phone_no[0]
	phone_no=user_phone_no[1]
	birthday=user_phone_no[2]
	age=user_phone_no[3]
	location=user_phone_no[4]
	if (location=="Abuja"):
		location="ABJ"
	elif (location=="Osun"):
		location="OSU"
	elif (location=="Kwara"):
		location="KWR"
	elif (location=="Kaduna"):
		location="KAD"
	elif (location=="Lagos"):
		location="LAG"
	elif (location=="Plateau"):
		location="PLA"
	else:
		pass
	n1=random.randint(10000,99999)
	reg_loc=location
	reg_loc1=str(reg_loc)
	b1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	b1=random.sample(b1,2)
	b1="".join(b1)
	c1=random.randint(00,99)
	c1=str(c1)
	n1=str(n1)
	license_no=reg_loc1+n1+b1.upper()+c1
	year_i=int(input("Enter the Number of years required e.g(3/5years): "))
	t=date.today()
	year=t.year
	month=t.month
	month=str(month)
	day=t.day
	day=str(day)
	current_year1=str(year)
	current_year=int(current_year1)
	e_year=current_year+year_i
	e_year=str(e_year)
	expiry_year=(e_year+"-"+month+"-"+day)

	print("""\t\t\t*********************************
		License Application Successfully
		**********************************
			Name:{}
			Phone Number:{}
			Birthday:{}
			Age:{}
			Locatiion:{}
			License Number:{}
			Expiry Date:{}

			""".format(name,phone_no,birthday,age,location,license_no,expiry_year))
	user[license_no]=name,phone_no,birthday,age,location,license_no,expiry_year
def status():
        license_no=input("Enter License Number: ")
        user_license_no=user[license_no]
        name=user_license_no[0]
        phone_no=user_license_no[1]
        birthday=user_license_no[2]
        age=user_license_no[3]
        location=user_license_no[4]
        license_no=user_license_no[5]
        expiry_year=user_license_no[6]
        if (license_no==user_license_no[5]):
        	pass
        else:
        	False
        print("*********************")
        print("This License is Valid")
        print("*********************")
        print("""
        Name:{}
	Phone Number:{}
	Birthday:{}
	Age:{}
	Locatiion:{}
	License Number:{}
	Expiry Date:{}	
		""".format(name,phone_no,birthday,age,location,license_no,expiry_year))

while(True):   
    print("Welcome to IsoloNG Driver's Lincensing Body\n To apply press\n")
    print("1. \tCreate Account\n2. \tApply for License\n3. \tCheck for Validity\n")
    response = input("Enter Response: \n")
    if(response=='1'):
        CreateAccount()
    elif(response=='2'):
        license_no()
    elif(response=='3'):
    	status()
    else:
        print("Invalid Response")
    ext=input("Do you want to carryout another operation?. Y/N: ")
    if(ext.upper()=='N'):
        print("Thank You.\n")
        break

		
