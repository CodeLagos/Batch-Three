"""Adebayo David
Email Address:Adebayodavid94@gmail.com
Phone Number:08162637190
Code Lagos Python Batch 3
Class 2 """
"""This code is a Pharmacy project that displays and compute the price and the quantity"""

print("Welcome to Theyvid's Pharmacy")
print("Select operation.")
print("David Adebayo's Project\nCode Lagos")
Select = int(input("1.Check Drug:\n2.Buy Drug:"))

if Select == 1: 
 print("Here is the drug we have;\nPharacetamol\nTetrasacline\nPlaster\nTramadol\nCough Serup\nPlaster\nMist Mag\nBlood Tonic\nVitamin C")
elif Select == 2:
	 print("Buy your drugs")
	 Drug_num = int(input("Please enter the number of Drugs: \n"))
	 Drug_list = [str(input("What is the Drug: " )) for count in range(Drug_num)]
	 Drug_price = [float(input("Enter the price of the Drug: \n")) for i in range(Drug_num)]
	 Drug_quan = [int(input("What is the quantity of Drug that you bought: \n")) for count in range(Drug_num)]
	 total = sum(int(quan * price) for quan, price in zip(Drug_quan, Drug_price))
	 print(total)
else:
    ext