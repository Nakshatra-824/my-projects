
dict = {
    123456 : "50,000",
    889900 : "30,000",
   
}
ui = int(input("enter your account number : "))
while True:
    if ui in dict:
        print("Press 1 to check balance")
        print("Press 2 to Deposit")
        print("Press 3 to withdraw")
        print("Press 4 to Exit")
        a = int(input(" : "))
        if a == 1:
            print("Your current balance is",dict.get(ui))
        elif a == 2:
            deposit = int(input("enter the amount you want to deposit : "))
            str_to_int = (dict.get(ui)).replace(",","")
            str_to_int = int(str_to_int)
            dict[ui] = str_to_int+deposit
            print(dict.get(ui))
        elif a == 3:
            wd = int(input("enter the amount you wanna withdraw :) "))
            str_to_int = (dict.get(ui)).replace(",","")
            str_to_int = int(str_to_int)
            dict[ui] = str_to_int-wd
            print(dict.get(ui))
        elif a == 4:
            break

    else:
        print("invalid number")
       

