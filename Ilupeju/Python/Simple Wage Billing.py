#Simple Daily Wage Billing program

start = int(input('Enter starting hour (0-23): '))
end = int(input('Enter ending hour (0-23): '))
if end >= start:
    print('Total Daily wage is  ', (end-start)*80 ,'Naira' )
else:
    print('Total Daily wage is ' , (24-start + end)*80, 'Naira') 
