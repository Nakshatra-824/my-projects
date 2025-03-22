user_input = input("enter weight you want to convert : ")
user_input = user_input.upper()
print(user_input)




if "F" in user_input:
    user_input  = user_input.replace("F","")
    user_input = int(user_input)
    user_input = (user_input - 32) * 5/9
    print(user_input)
elif "C" in user_input:
    user_input  = user_input.replace("C","")
    user_input = int(user_input)
    user_input = (user_input*9/5) + 32
    print(user_input)