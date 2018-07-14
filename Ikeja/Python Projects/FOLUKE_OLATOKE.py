





        
    
print('Welcome to Guessing Game')
print('The range is from 1 to 200')
print('START')
import random
x = random .randint(1,200)
count = 0
while count<7:
    y = int(input("Enter any number from 1 to 200:"))
    
    if y == x :
        print(y ,"is correct")
        break
    elif y> x:
        
        print(y, 'is too high')
    else:
        y<x
        print(y,' is too small')
    
    if count < 5:
        print('You have' ,str(6-count),' attempts more')
    elif count ==5:
        print('You have ONE more attempt')
    elif count ==6:
        print('GAME OVER')
    count = count + 1
            
    
               
        
      

      
    
    
             
