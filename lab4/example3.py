numb1 = input("Enter number 1:")
numb2 = input("Enter number 2:")
count = 0
for i in range(len(str(min(int(numb1), int(numb2))))):
    if len(numb1) > len(numb2):
        if numb1[(len(numb1) - len(numb2)) + i] == numb2[i]:
            count += 1
    elif len(numb1) < len(numb2):
        if numb2[(len(numb2) - len(numb1)) + i] == numb1[i]:
            count += 1
    elif len(numb1) == len(numb2):
        if numb1[i] == numb2[i]:
            count += 1
print(count)   