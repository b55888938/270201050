question_numb = int(input("How many numbers do you want to input?"))
even = 0
odd = 0
count = 0
while count < question_numb:
    count += 1
    a = int(input("Enter an integer"))
    if a % 2 == 0:
        even += a
    else:
        odd += a
total = odd + even
print(100 * even / total)