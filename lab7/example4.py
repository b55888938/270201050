def binary_to_dec(wanted):
    sum = 0
    wanted = wanted[::-1]
    for i in range(len(wanted)):
        sum += int(wanted[i]) * (2**i)
    return sum
def dec_to_binary(sum):
    wanted = ""
    while sum > 0:
        wanted += str(sum%2)
        sum //= 2
    return wanted[::-1]
def main():
    wanted = "10010"
    print(binary_to_dec(wanted))
    sum = 18
    print(dec_to_binary(sum))
main()





