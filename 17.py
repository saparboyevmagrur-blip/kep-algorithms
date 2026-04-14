def sum_of_digits(number):
    sum = 0
    for digit in str(number):
        sum += int(digit)

    return sum

# print(sum_of_digits(185)) # 14
for n in range(1000, 10000):
    if sum_of_digits(n) % 2 == 0:
        print(n, end=" ")