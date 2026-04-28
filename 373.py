n = int(input())
royxat = list(map(int, input().split()))
# max_value = max(royxat)
# print(max_value)
max_value = royxat[0]
for son in royxat:
    if son > max_value:
        max_value = son

print(max_value)
# 19 38 -5 89 10
# max_v = 19
# 1-q: son = 19; 19 > 19 => False
# 2-q: son = 38; 38 > 19 => True; max_v = 38
# 3-q: son = -5; -5 > 38 => False;
# 4-q: son = 89; 89 > 38 => True; max_v = 89
# 5-q: son = 10; 10 > 89 => False;
# sikl tugadi; max_v = 89

min_value = royxat[0]
for son in royxat:
    if son < min_value:
        min_value = son

print(min_value)