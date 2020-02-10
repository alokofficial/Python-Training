def tcase(n):

    if len(n)<=1:
        print("palindrome")
    else:
        if n[0]==n[-1]:
            tcase(n[1:-1])
        else:
            print("not palindrome")
test=input("enter the string to check palindrome\n")
tcase(test)
