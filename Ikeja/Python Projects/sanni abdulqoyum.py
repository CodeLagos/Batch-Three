import random
def guess():
    print("exit")

print("welcome")
name= str(input("please enter name "))
c = 1
random_number = random.randint(0, 50)
while  c <= 10:
    c = c+1
    user_number =int(input(name+ " enter a mumber greater than 0 but less than 50 "))
    if random_number == user_number:
        print(name+" you guessesd right")
        print( " congratulation")
        break
    if user_number > random_number:
        print(name+" that is too high")
    if user_number > 50:
        print("the number is above 50 try")
    if user_number < random_number:
        print(name+" thst is too low")
    if c == 9:
        print("this is your final guess")
    if c == 10:
        print("game over you have run out of tries")
        break

                  
                  
               
   
                
guess()
