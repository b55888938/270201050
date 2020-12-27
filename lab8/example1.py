def harmonic(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return 1/n + harmonic(n-1)
a = int(input("Enter an integer."))
print(harmonic(a))