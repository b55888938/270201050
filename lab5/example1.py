mail = 'ceng113@example.com'
e_mail = input('Enter your e-mail\n').lower()
parts_of_mail = email.split('@')
parts_of_mail[0] = parts_of_mail[0].replace('.','')
last_mail = parts_of_mail[0]+'@'+parts_of_mail[1]
if last_mail == e_mail:
    print("true")
else:
    print("false")

