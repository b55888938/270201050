def level_password(password):
    if " " in password or len(password) < 8:
        return "Level 0"
    elif password.isalpha() or password.isnumeric():
        return "Level 1"
    elif password.isalnum():
        return  "Level 2"
    else:
        return "Level 3"
user_pass = input("Enter a password:\n")
print(level_password(user_pass))
