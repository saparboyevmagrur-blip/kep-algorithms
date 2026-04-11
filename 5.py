# 1 + 2 + 3 + 4 + ... + (n - 1) + n
# n = int(input())
# s = 0
# for son in range(1, n + 1):
#     s += son # s = s + son

# print(s)
# Example: n = 5
# Sikl qadamlari:
# 1. son = 1; 0 + 1 = 1 = s
# 2. son = 2; 1 + 2 = 3 = s
# 3. son = 3; 3 + 3 = 6 = s
# 4. son = 4; 6 + 4 = 10 = s
# 5. son = 5; 10 + 5 = 15 = s
# Natija: s = 15

import math
n = int(input())
s = 0
for son in range(1, n + 1):
    s += int(math.sqrt(son))

print(s)