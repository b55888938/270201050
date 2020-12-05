password = "abc123"
while True:
    a = input("Please enter the password.")
    if a == "abc123":
        print("Welcome")
        break
    elif a == "help":
        print(password[0])
    else:
        print("Wrong")
