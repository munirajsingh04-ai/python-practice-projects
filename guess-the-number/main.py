import random
target = random.randint(1,100)


while True:
    userChoice = int(input("Guess the target or Quit(Q): "))
    if(userChoice=="Q"):
        break
    userChoice = int(userChoice)
    if(userChoice==target):
        print("Success:Correct Guess!")
        break
    elif(userChoice<target):
        print("your number is too small guess again...")
    else:
         print("your number is too big guess again...")


         print("-----GAME OVER-----")
    
