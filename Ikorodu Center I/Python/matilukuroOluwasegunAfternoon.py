#Welcome Message
print("=======================================================================")
print("           ","****Welcome To Our Red Blood Cell Compatibility Guide****")
print("=======================================================================")
print("           ","****A Project Work Done By: Matilukuro Oluwasegun****")
print("=======================================================================")
print("                                                                     ")
print ("Note:")
#This takes the blood group of the user
print("For A+ input '1', For B+ to input '2', For AB+ input '3', For O+ input '4'")
print("For A- input '5', For B- input '6', For AB- input '7', For O- input '8'")
print ("                                                                    ")

#This command takes the details of the user
fname = input("Please Enter Your First Name:")
lname = input("Please Enter Your Last Name:")
#Prompt User to Input Corresponding Blood Group
user_input = input("Please input figure corresponding to your Blood Group:")
#Conditional Statement for User Input

if user_input == '1':    
      print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
      print ("Your Blood Group is A+")
      print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++")     
      print ("You can receive blood from: A+, A-, O+, O-")
      print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++")      
      print ("You can donate blood to: A+, AB+")
      print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++")      
      print ("Thank You", fname, lname, "For Using Our Red Blood Cell Compatibility Guide")
      print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
 
elif user_input == '2':
      print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++")      
      print ("Your Blood Group is B+")
      print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
      print ("You can receive blood from: B+, B-, O+, O-")
      print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++")      
      print ("You can donate blood to: B+, AB+")
      print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
      print ("Thank You", fname, lname, "For Using Our Red Blood Cell Compatibility Guide")
      print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
 
elif user_input == '3':
      print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++")      
      print ("Your Blood Group is AB+")
      print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++")      
      print ("You can receive blood from: Everyone")
      print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++")      
      print ("You can donate blood to: AB+")
      print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++")      
      print ("Thank You", fname, lname, "For Using Our Red Blood Cell Compatibility Guide")
      print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
 
elif user_input == '4':
      print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++")      
      print ("Your Blood Group is O+")
      print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
      print ("You can receive blood from: O+, O-")
      print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
      print ("You can donate blood to: O+, A+, B+, AB+")
      print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
      print ("Thank You", fname, lname, "For Using Our Red Blood Cell Compatibility Guide")
      print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
 
elif user_input == '5':
      print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
      print ("Your Blood Group is A-")
      print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
      print ("You can receive blood from: A-, O-")
      print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
      print ("You can donate blood to: A+, A-, AB+, AB-")
      print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
      print ("Thank You", fname, lname, "For Using Our Red Blood Cell Compatibility Guide")
      print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++")

elif user_input == '6':
      print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
      print ("Your Blood Group is B-")
      print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
      print ("You can receive blood from: B-, O-")
      print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
      print ("You can donate blood to: B+, B-, AB+, AB-")
      print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
      print ("Thank You", fname, lname, "For Using Our Red Blood Cell Compatibility Guide")
      print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
      
elif user_input == '7':
      print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
      print ("Your Blood Group is AB-")
      print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
      print ("You can receive blood from: A-, B-, AB-, O-")
      print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
      print ("You can donate blood to: AB+, AB-")
      print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
      print ("Thank You", fname, lname, "For Using Our Red Blood Cell Compatibility Guide")
      print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++")

elif user_input == '8':
      print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
      print ("Your Blood Group is O-")
      print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
      print ("You can receive blood from: O-")
      print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
      print ("You can donate blood to: Everyone")
      print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
      print ("Thank You", fname, lname, "For Using Our Red Blood Cell Compatibility Guide")
      print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++")

else:
    print ("Invalid input")
