numb = input("Please enter a number.")
a = len(numb)
sum = 0
if int(numb[a-2]) == 0:
  for i in range (a-1 ,a):
    sum += int(numb[i])
  print(sum)
else:
  for i in range (a-2 ,a):
    sum += int(numb[i])
  print(sum)