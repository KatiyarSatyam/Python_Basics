#decision control
#correct email- xyz@gmail.com
#correct password - 1234
username = input("Enter your username: ")
email = input("enter your email: ")
password = input("enter your password: ")
if '@' in email:
    password = input("enter your password: ")

    if email =="xyz@gmail.com" and password == "1234":
        print(f"Welcome {username}")
    elif email =="xyz@gmail.com" and password !="1234":
        print("Incorrect password")
        password = input("enter your password: ")
        if password =="1234":
            print("correct password")
        else:
            print("Incorrect password")
    elif email !="xyz@gmail.com" and password =="1234":
        print("Incorrect email")
        email = input("enter your email: ")
        if email =="xyz@gmail.com":
            print(f"Welcome {username}")
        else:
            print("Incorrect email")
    else:
        print("Incorrect email or password")
else:
    print("email is wrong. !Try again!")