b = int(input('Enter a number:\n'))
list =[]
for i in range(b):
    c = [0]* b
    c[i]=1
    list.append(c)
for k in list:
    print(k)