#ONAFUWA AYOOLUWA
#CODELAGOS IGBOGBO,IKORODU.
#This programme is named 'financial report manager'. It's fucntion is to collect daily financial report from the user and analyse such input and be able to deduce if the financial report for the day is balanced.It computes the data inputted by the user and save a copy of the financial report on the computer for the user's future reference. The saved data might as well be accessible using this programme or by digging directly into the computer’s directory.
#THIS PROJECT WAS CARRIED OUT SUCCESSFULLY WITH THE USE OF THE FOLLOWING: function,while loop,for loop,input,conditionals,list,dictionary,files,exception & string formatting
#credit to Mr.Rex and my code lagos broskis,God bless you fam


#define a function to create a dictionary from two lists
def a(x,y):
    noi={}
    d=[]
    pos=0
    count=1
    for i in x:
        d.append([i])
    for i in y:
        invoc=d[pos]
        invoc.append(i)
        pos+=1
    for i in d:
        noi[count]=i
        count+=1
    return noi

while True:
 try:
     #collect input from the user on the operation to be performed
    print('MENU \n To enter a new record press 1 \n To retrieve an old record press 2 \n Exit program press 3')
    option=str(input('Enter an option: '))
    #create a new file and store the input of the user
    if option=='1':
        new_file=input('Enter date. (e.g mm-dd-yr): ')
        start_up_capital=int(input('Enter your startup capital: '))
        supplementary_capital=int(input('Enter your supplementary capital: '))
        capital=(start_up_capital) + (supplementary_capital)
        balance=int(input('Enter balance: '))
        invoice_amount=[]
        rate_amount=[]
        n_invoice=int(input('Enter total number of invoice: '))
        for i in range(n_invoice):
            invoice=int(input('Enter invoice amount: '))
            if invoice<=5000:
                rate=100
                invoice_amount.append(invoice)
                rate_amount.append(rate)
            elif invoice>=5001 and invoice<=10000:
                rate=200
                invoice_amount.append(invoice)
                rate_amount.append(rate)
            elif invoice>=10001 and invoice<=20000:
                rate=300
                invoice_amount.append(invoice)
                rate_amount.append(rate)
            elif invoice>=20001 and invoice<=30000:
                rate=400
                invoice_amount.append(invoice)
                rate_amount.append(rate)
            elif invoice>=30001 and invoice<=40000:
                rate=500
                invoice_amount.append(invoice)
                rate_amount.append(rate)
            elif invoice>=40001 and invoice<=50000:
                rate=500
                invoice_amount.append(invoice)
                rate_amount.append(rate)
            elif invoice>=50001 and invoice<=60000:
                rate=600
                invoice_amount.append(invoice)
                rate_amount.append(rate)
            elif invoice>=60001 and invoice<=70000:
                rate=700
                invoice_amount.append(invoice)
                rate_amount.append(rate)
            elif invoice>=70001 and invoice<=80000:
                rate=800
                invoice_amount.append(invoice)
                rate_amount.append(rate)
            elif invoice>=80001 and invoice<=90000:
                rate=800
                invoice_amount.append(invoice)
                rate_amount.append(rate)
            elif invoice>90001 and invoice<=100000:
                rate=1000
                invoice_amount.append(invoice)
                rate_amount.append(rate)
            elif invoice>100000:
                rate=int(input('Enter rate: '))
                invoice_amount.append(invoice)
                rate_amount.append(rate)
        total_amount_spent=sum(invoice_amount)
        total_rate=sum(rate_amount)
        cash_left=capital - (sum(invoice_amount))
        deficit=cash_left - balance
        mod=a(invoice_amount,rate_amount)
        if cash_left==balance:
            print('ACCOUNT BALANCED')
            file=open('{0}{1}'.format(new_file,'.txt'),'w')
            file.write('AOLONA DAILY REPORT   {7} \n \n START-UP CAPITAL: {0} \n SUPPLEMENTARY CAPITAL: {1} \n TOTAL CAPITAL: {2} \n CASH LEFT: {3} \n TOTAL INVOICE: {4} \n TOTAL RATE: {5} \n INVOICE/RATE: {6} \n \n REMARKS: ACCOUNT IS CERTIFIED AS BALANCED'.format(start_up_capital,supplementary_capital,capital,balance,total_amount_spent,total_rate,mod, new_file))
            file.close()
        else:
            print('ACCOUNT NOT BALANCED, DEFICIT OF', deficit, 'naira')
            file=open('{0}{1}'.format(new_file,'.txt'),'w')
            file.write('AOLONA DAILY REPORT   {7} \n \n START-UP CAPITAL: {0} \n SUPPLEMENTARY CAPITAL: {1} \n TOTAL CAPITAL: {2} \n CASH LEFT: {3} \n TOTAL INVOICE: {4} \n TOTAL RATE: {5} \n INVOICE/RATE: {6} \n \n REMARKS: ACCOUNT IS CERTIFIED AS NOT BALANCED,DEFICIT OF {8}'.format(start_up_capital,supplementary_capital,capital,balance,total_amount_spent,total_rate,mod,new_file,deficit))
            file.close()
        print('RECORD SAVED')
        print('RETURNING TO MENU..........') 
        #read previously saved files  
    elif option=='2':
        file_name=input('Enter the date of the record to retrieve (e.g mm-dd-yr): ')
        file=open('{0}{1}'.format(file_name,'.txt'),'r')
        print(file.read())
        file.close()
        print('RETURNING TO MENU..........')
        #end program
    elif option=='3':
        print('GOODBYE!!')
        break
    else:
        print('invalid option \n Please read through the menu options')
 except:
     print('SORRY,AN ERROR OCCURRED')

        

            
            
            
               
               
               
            