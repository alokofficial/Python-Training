email=input("Enter your email")
if'@'in email:
    #paste here

    password=input("Enter your password")
    if email=="hit@gmail.com" and password=="12345":
       print("login successful")
    elif email=="hit@gmail.com" and password!="12345":
        print("incorrect password")
        password=input("enter password again")
        if password=="12345":
            print("welcome")
        else:
            print("rhne de tere se na ho payega")
    else:
        print("incorrect credential")


else:
    print("gawaar")
