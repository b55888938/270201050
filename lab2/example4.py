n_ticket = 3
y_th_6_o_t_60 = 0
bt_6_18 = n_ticket / 2
age = int(input("Enter your age:\n"))
if age <= 6:
  print("Your price is" + y_th_6_o_t_60)
elif age > 6 and age < 18:
  print("Your price is" + bt_6_18)
elif age >= 18 and age < 60:
  print("Your price is" + n_ticket)
elif age >= 60:
  print(y_th_6_o_t_60)     