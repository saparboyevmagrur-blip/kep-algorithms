# n ta son berilgan
# 1. toq sonlar (if 2 ga bo'lganda != 0 yoki == 1)
# 2. s += son
n = int(input())
s, i = 0, 0
# for i in range(n):
#     a = int(input())
#     if a % 2 == 1:
#         s += a

while i < n:
    a = int(input())
    if a % 2 == 1:
        s += a
    i += 1
print(s)