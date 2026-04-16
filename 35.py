a = int(input())
b = int(input())
if a > b:
    a, b = b, a

count = 0
for n in range(a, b + 1):
    if n % 4 == 0:
        count += 1
print(count)
