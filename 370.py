n = int(input())
royxat = list(map(int, input().split()))

for index in range(len(royxat)):
    if (index + 1) % 2 != 0:
        print(royxat[index], end=" ")