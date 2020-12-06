password = input("Please enter a password.")
numbs = "0123456789"
for i in password:
    if i in numbs:
        if len(password) > 8 and password.lower() != password and password.upper() != password:
            print("Valid")
        else:
            print("İnvalid")
            break
    else:
        print("İnvalid")
        break