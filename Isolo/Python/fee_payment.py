#Fees Payment Code
#NAME: SALAUDEEN HIBATULLAH ADEKUNLE
#EMAIL:hibatus2002@yahoo.com
#PHONE NUMBERS:08054208775,08026406908,07032877925
#PROGRAMME/BATCH:CODE LAGOS PYTHON BATCH 3 CLASS 2
#DESCRIPTION OF THE PROJECT:The code displays amount to be paid for a particular programme,takes in amount to be paid and displays the balance and excess payments,when there is any


print("WELCOME TO KAYLORD EDUCATIONAL INSTITUTE\nYOUR SUCCESS IS GUARANTEED")
print()

programmes_costs = [
    ['WAEC', 2000],
    ['POST UME', 5000],
    ['JAMB', 10000],
    ['ICAN', 30000],
]

def request_payment(x):
    amount = x
    print("You are to pay N{}".format(str(amount)))
    payment = int(input("Enter Amount To Pay \n"))

    bal = amount - payment
    excess = payment - amount
    print("You just paid ", str(payment))

    if bal > 0:
        print("Your balance is", str(bal))
    if bal < 0:
        print("Note: You have over paid by",str(excess))
        print("You have sucessfully registered for the programme. Your excess payment is", str(abs(excess)))
        val = input("Type q to quit or any other key to register for another programme\n")
        if val.strip() == "q":
            print("Bye", name)
            exit()
    else:
        print("You have sucessfully registered for the programme. Your balance is", str(abs(bal)))
        val = input("Type q to quit or any other key to register for another programme\n")
        if val.strip() == "q":
            print("Bye", name)
            exit()


def select_program():
    for i, k in enumerate(programmes_costs):
        print("{}. {} => N{}".format(i,k[0], k[1]))
    return input("Enter 'q' to quit the program\n")

quit_program = False
has_entered_name = False

while quit_program == False:
    name = input("Hello, Enter Your Full Name \n")
    email = input("Enter Your Email Address: ")
    Phone_Number = input("Enter Your Phone Number: ")
    print("\nWelcome {}. \nPlease Select Your Desired programme\n".format(name))

    selected_program = select_program()

    try:
        selected_program = int(selected_program)
        if selected_program >= 0 and selected_program < 4:
            cost = programmes_costs[selected_program][1]
            request_payment(cost)
        else:
            print("Sorry, we do not offer anything like that. Try again")
    except ValueError:
        if selected_program.strip() == "q":
            quit_program = True
        else:
            print("Sorry, we do not offer anything like that. Try again")

print("Bye", name)
