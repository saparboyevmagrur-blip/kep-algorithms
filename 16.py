# !n = 1 * 2 * 3 * 4 * ... * (n - 1) * n 
n = int(input())
s = 1
for son in range(1, n + 1):
    s *= son

print(s)