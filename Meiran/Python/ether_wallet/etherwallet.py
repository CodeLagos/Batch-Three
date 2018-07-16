import random

pk = [
    "a7b38c8e8f7ac828c898d9f9938c982a682cd882e85a883cdff828a73bc6d8af", 
    "988fb6d6a7c993be6de6acc8275dbcb925cadf993d635ade7bc77d7ab8737acd", 
    "ac72cdb73dea8fb83da443daceb826cad423abc883cae5ce73ba32b74ca54abe", 
    "b838af73be992cae93bd8627acbe9937a53cbed77fa72fa543b9289bac3298c5",
    "d7838ac84be82bce42abe9938ace8626bd83ffe42197abc52319acdff187ba6d",
    "abd893a3bace938bd8839abde6a67ba538bc93ac2549de9365ad9b93de92abd8"
]
eth = [
    "0.23532",
    "0.04323",
    "1.2211",
    "0.9973",
    "2.0",
    "0.4325"
]

def create():
    print("[1]Create wallet \n[2]Check wallet info \n[3]Send token \n[4]List out Private keys")
    opt = input("Input your option: ")
    if opt == "1":
        print("Generating Private Key.....")
        pkRan = random.choice(pk)
        print("\t" + pkRan + "\nPrivate Key Successfully Generated.")
        create()
    elif opt == "2":
        userPk = input("Paste Your Private Key: ")
        i = 0
        for i in range(len(pk)):
            if userPk == pk[i]:
                print("Welcome, User.")
                print("Wallet Balance: " + eth[i] + " ETH")
                break
        print("Invalid Private Key.")
    elif opt == "3":
        userPk = input("Paste Your Private Key: ")
        j = 0
        for j in range(len(pk)):
            if userPk == pk[j]:
                print("Welcome, User.")
                print("Wallet Balance: " + eth[j] + " ETH")
                def send():
                    amt = input("Please Enter The Amount To Send: ")
                    if amt > eth[j]:
                        print("Insufficient balance :(")
                        send()
                    else:
                        eth[j] = float(eth[j]) - float(amt)
                        print("Sent Successfully :)")
                        print("Your Current Balance Is " + str(eth[j]) + " ETH")
                send()
        print("Invalid Private Key.")
    elif opt == "4":
        k = 0
        for k in range(len(pk)):
            print("[" + str(k+1) + "] " + pk[k])
        print("Done!!!")
        def que():
            ques = input("Do yout want to continue?  Yes or No: ")
            conf = ques.lower()
            if conf == "yes":
                create()
            elif conf == "no":
                print("Goodbye")
            else:
                print("Invalid input... Try again")
                que()
        que()
    elif opt > 4:
        print("Invalid Option.")
create()