gpa = float(input("Enter your GPA:\n"))
numb_lect = int(input("Enter your number of lectures:\n"))
if gpa >= 0 and numb_lect >= 47:
  print("GRADUATED!!!")
elif gpa >= 0 and numb_lect < 47:
  print("Not enough number of lectures!")
elif gpa < 0 and numb_lect >= 0:
  print("Not enough GPA!")
else:
  print("Not enough GPA and Number of lectures!")    