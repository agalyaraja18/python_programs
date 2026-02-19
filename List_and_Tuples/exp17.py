password=input("Enter your password:")
a=0
while a<3:
    user_input=input("Enter the password:")
    if user_input==password:
        print("Unlocked")
        break
    else:
        a+=1
    print("Locked")