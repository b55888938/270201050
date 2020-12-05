leap_year = int(input("Please enter a year to chech it's leap year or not:\n"))
if leap_year % 4 == 0:
  if leap_year % 100 == 0:
    if leap_year % 400 != 0:
      print("It's not a lap year.")
  print("It's a lap year.") 