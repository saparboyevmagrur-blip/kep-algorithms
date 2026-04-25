# my_list = [18, 15, 20, 92, 1000]
# for element in my_list:
#     print(element, end = " ")

# print(*my_list)


n = int(input())
royxat = list(map(int, input().split()))
royxat.reverse()
print(*royxat)

