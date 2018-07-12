# acount number =  112233 , pin = 234234
# account number = 234234 , pin = 332211 


account_num = ['112233','332211']
account_pin = ['234234','432432']
account_name =['jay','kola','femi']
account_balance = ['3500','4000']
more = True

print("Hello!!! welcome to our bank ")
account = (input("please enter your account \n"))
while account not in account_num:
    print ("it seems you dont have an account with us please register at our nearest branch ")
    account = (input("please enter your account \n"))
account_num_index = account_num.index(account)
print (account_num_index)
pin = input("please enter your pin \n")
while pin != account_pin[account_num_index]:
    print("invalid pin selected")
    pin = input("please enter your pin \n")
print ("welcome " , account_name[account_num_index])
while more is True  :
	print("")
	print ("1 -> Balance")
	print ("2 -> Transfer")
	print ("3 -> Deposit")
	print ("4 -> End")
	
	transaction = (input("SELECT YOUR TRANSACTION CODE \n"))
	if transaction is '4' :
		print("Thank you for banking with us")
		break
	if transaction is  '1':
		print("your account balance is " , account_balance[account_num_index] , "Naira")
		print("")
		print("do you still want to perform another operation ? ")
		print("1 -> Continue")
		print("2 -> End")
		con =  int(input('\n'))
	  
	if transaction is '2':
		con = 1 # to keep the value of con as 1 or more as true from line 
		print("code"  + "\t"+ "Banks") 
		print("1" + "\t" + "Zenith Bank") 
		print("2" + "\t" + "Union Bank") 
		print("3" + "\t" + "Access Bank")
		print("4" + "\t" + "Guaranty Trust Bank")
		print("5" + "\t" + "UBA")
		print("6" + "\t" + "Cancel")
		select_bank = input("Select Bank to transfer your fund \n")
		if select_bank is '6':
			print("1 -> No")
			print("2 -> Yes")
			print('')
			con = int(input("Are you sure you want to cancel this transaction \n"))
			if con is 1:
				more = True
			if con is 2:
				print("Thank You For Banking With Us")
				break
		if select_bank is '1': 
			bank = "Zenith Bank"
		elif select_bank is '2':
			bank = "Union Bank"
		elif select_bank is '3' :
			bank = "Access Bank"
		elif select_bank is '4' :
			bank = "Guaranty trust Bank"
		elif select_bank is '5':
			bank = "UBA"
		else :
			select_bank = '0'
		while select_bank is '0' :
			print("")
			print("Invalid Bank Selected , please select bank in range 1 - 5 and 6 to cancel transaction")
			print("code"  + "\t"+ "Banks") 
			print("1" + "\t" + "Zenith Bank") 
			print("2" + "\t" + "Union Bank") 
			print("3" + "\t" + "Access Bank")
			print("4" + "\t" + "Guaranty Trust Bank")
			print("5" + "\t" + "UBA")
			print("6" + "\t" + "Cancel")
			select_bank = input("Select Bank to transfer your fund \n") 
			if select_bank is '1': 
				bank = "Zenith Bank"
			elif select_bank is '2':
				bank = "Union Bank"
			elif select_bank is '3' :
				bank = "Access Bank"
			elif select_bank is '4' :
				bank = "Guaranty trust Bank"
			elif select_bank is '5':
				bank = "UBA"
			else :
				select_bank = '0'
		while True:
			try :	
				an = int(input("Enter account number to transfer to \n"))
				break
			except ValueError:
				print("Account number must be a number")
		while True :
			try :
				amount = int(input("Enter Amount to transfer \n"))
				break
			except ValueError:
				print("Invalid Amount Entered")
				
		print("You are Transferring " , amount , "Naira to account number " , an , " " , bank, )  
	
		print("1 -> No")
		print("2 -> Yes")
		print('')
		tsure = input("Do you want to continue ? \n")
		if tsure is '1' :
			print("")
			print("Transaction Aborted")
			more = True 
		if tsure is '2' and amount > int(account_balance[account_num_index]) :
				print('')
				print("Transfer Failed")
				print('')
				print("Insufficient Balance")
				more = True
		if tsure is '2' and amount <= int(account_balance[account_num_index]) :
				print('')
				print("Transfer Successful")
				print('')
				newbalance = int(account_balance[account_num_index]) - amount
				print("your new balance is " , newbalance )
				account_balance[account_num_index] = newbalance  
		
		if tsure is not '1' and tsure is not '2' :
			print("Transaction Aborted")
			print("Invlid code selected")
		
	if transaction is '3':
		con = 1 # to keep the value of con as 1 or more as true from last line
		deposit = int(input("Enter Amount to deposit \n"))
		print("You are depositing " , deposit , "Naira to your account " )  
		print("1 -> No")
		print("2 -> Yes")
		print('')
		tsure = input("Do you want to continue ? \n")
		if tsure is '1' :
			print("")
			print("Transaction Aborted")
			more = True 
		if tsure is '2' :
			print ("Transaction Successful")
			newbalance =  int(account_balance[account_num_index]) + deposit
			print("your new balance is" , newbalance)
			account_balance[account_num_index] = newbalance  
	if transaction is not '1' and transaction is not '2' and transaction is not '3' and transaction is not '4' :
		con = 1
		print("Invalid code selection, please try again")
	if con is 1   :
		more = True 
	if con is 2  :
		more = False
		print("Thank You For Banking With Us")


