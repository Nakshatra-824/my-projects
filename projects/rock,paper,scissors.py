import random

ui = int(input("enter the number : "))

options = {
    1 : "rock",
    2 : "scissors",
    3 : "paper"
}
num,value = random.choice(tuple(options.items())) 

if (ui>3):
    print("invalid number")
elif(ui == 1 and num == 2):
    print(value)
    print("you win !")
    
elif(ui == 1 and num == 3):
    print(value)
    print("you lose !")
    
elif(ui == 1 and num == 1):
    print(value)
    print(" Tie !")


elif(ui == 2 and num == 1):
    print(value)
    print("you lose !")
    
elif(ui == 2 and num == 3):
    print(value)
    print("you win !")
    
elif(ui == 2 and num == 2):
    print(value)
    print(" Tie !")
    
    
elif(ui == 3 and num == 1):
    print(value)
    print("you win !")
    
elif(ui == 3 and num == 2):
    print(value)
    print("you lose !")
    
elif(ui == 3 and num == 3):
    print(value)
    print(" Tie !")
    
    






