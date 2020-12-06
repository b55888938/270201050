mail = input("Enter an e-mail adress.")
mail_2 = mail.lower()
mail_3 = mail_2.split("@")[0]
mail_4 = mail_3.replace(".","") + "@" + mail_2.split("@")[1]
if mail_4 == "ceng113@example.com":
    print("true")
else:
    print("false")