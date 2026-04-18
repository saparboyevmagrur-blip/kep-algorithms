# "123" => "1", "2", "3" => 1, 2, 3
def sum_digits(number):
    s = 0
    for digit in str(number):
        raqam = int(digit)
        s += raqam # s = s + raqam

    return s

print(sum_digits(123)) # 6
print(sum_digits(357)) # 15

# number = 357 => "357"
# Sikl qadamlari(iteratsiyasi)
# 1. d = "3"; => r = 3; s = 0 + 3 = 3
# 2. d = "5"; => r = 5; s = 3 + 5 = 8
# 3. d = "7"; => r = 7; s = 8 + 7 = 15
# s = 15