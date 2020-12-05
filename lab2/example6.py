a = eval(input("Enter a number for coeffiecent of x^2:\n"))
b = eval(input("Enter a number for coeffiecent of x:\n"))    
c = eval(input("Enter a number for coeffiecent:\n"))
delta_sqrr =  ((b**2) - (4*a*c))**(1/2)
root_1 = (-b + delta_sqrr) / (2*a)
root_2 = (-b - delta_sqrr) / (2*a)
if a == 0:
  print("There is only one root and it's", ((-1 * c) / b) )
  if b == 0:
    print("There is no root.")
else:
  print("Root1 and root2 are",root_1,",",root_2        