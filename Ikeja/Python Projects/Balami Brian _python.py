import random
numofguesses = 0

print("Hello, what is your name")
name = input()

number = random.randint(1,100)
print("Number I an thinking of is between 1 and 100" ,name)

while numofguesses < 6:
    print("Take a Guess. ")
    guess = input()
    guess = int(guess)

    numofguesses = numofguesses + 1
    if guess < number:
                print("Number is too low")
    if guess > number:
                print("Number is too high")
    if guess == number:
        break
if guess == number:
                numofguesses = str(numofguesses)
                print("well done " ,name,"You gussed the number in: " , numofguesses)

if guess != number:
                      number = str(number)
                      print("wrong! unlucky, the numbeer was: " ,number)
                


