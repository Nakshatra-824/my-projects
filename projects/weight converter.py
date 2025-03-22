user_input = input("enter weight you want to convert : ")
user_input.lower()


if "kg" in user_input:
    user_input  = user_input.replace("kg","")
    user_input = float(user_input)
    user_input*= 2.20462
    print(user_input)
elif "lb" in user_input:
    user_input  = user_input.replace("lb","")
    user_input = float(user_input)
    user_input*= 0.453592
    print(user_input)

# Done!