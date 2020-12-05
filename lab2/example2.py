a = int(input("Enter a number"))
b = int(input("Enter a number"))
c = int(input("Enter a number"))
if c < a and c < b:
    print(c)
elif b < a and b < c:
    print(b)
elif a < b and a < c:
    print(a)
else:
    print(a)
