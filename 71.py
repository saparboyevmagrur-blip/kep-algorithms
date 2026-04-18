def sum_digits(number):
    s = 0
    for digit in str(number):
        raqam = int(digit)
        s += raqam # s = s + raqam

    return s

n = input()
n1 = n[0:3]
n2 = n[3:6]
print(sum_digits(n1) == sum_digits(n2))