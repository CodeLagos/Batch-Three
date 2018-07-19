name = str(input("enter your name "))
import random
def guess():
    print("Game over")
    

print("hello", name)
counter = 1
random_number = random.randint(0, 50)
while counter > 0 and counter <= 7:
    counter = counter+1
    number =int(input(name+ " enter a number greater than 0 but less than 50 "))
    if random_number == number:
        print(name+" you guessed right")
        print ("congratulations")
        break
    if number > random_number:
        print(name+" that number is too high try again")
             
    if number < random_number:
        print(name+" thst number is too low try again")
        
    if counter == 7:
        print(name+" you have run out of guesses")
        break

               
guess()

