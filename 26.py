# 1-usul:
# n = int(input())
# count = 0
# for son in range(1, n + 1):
#     if son % 12 == 0 or son % 5 == 0:
#         count += 1

# print(count)
# TL - time limited

# 2-usul:
# 1, 2, 3, ..., 23, 24, ..., 59, 60 
# n // 12 = 60 // 12 = 5
# n // 5 = 60 // 5 = 12
# n // 12 + n // 5 - n // 60
# 5 + 12 - 1 =  16
n = int(input())
print(n // 12 + n // 5 - n // 60)
