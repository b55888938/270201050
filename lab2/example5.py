month = input("Please enter a month:\n")
day = int(input("Please enter a number for day:\n"))
if month == "march" and day >= 20:
  print("Spring")
elif month == "april" or month == "may":
  print("Spring")
elif month == "june" and day < 21:
  print("Spring")
elif month == "june" and day >= 21:
  print("Summer")
elif month == "july" or month == "august":
  print("Summer")
elif month == "september" and day < 22:
  print("Summer")
elif month == "september" and day >= 22:
  print("Fall")
elif month == "october" or month == "november":
  print("Fall")
elif month == "december" and day < 21:
  print("Fall")
elif month == "december" and day >= 21:
  print("Winter")
elif month == "january" or month == "february":
  print("Winter")
elif month == "march" and day < 20:
  print("Winter")  