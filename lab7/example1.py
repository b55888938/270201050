def funct(number):
    sum = 0
    for i in range(number):
        sum += a_list[i]
    return sum**2


a_list = [12, -7, 5, -89.4, 3, 27, 56, 57.3]
a = funct(len(a_list))
print(a)