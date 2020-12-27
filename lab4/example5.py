
numb_numb = int(input("How many fibonacci numbers?"))
sum_1 = 0
sum_2 = 1
print(sum_1)
print(sum_2)
for i in range(numb_numb - 2):
    sum_3 = sum_1 + sum_2
    sum_1 = sum_2
    sum_2 = sum_3
    print(sum_3)