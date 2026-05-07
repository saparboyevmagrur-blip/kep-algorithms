# map(func, iterable)
def divisors_count(son):
    # natural bo'luvchilari: 1, 2, ... 9, ...son
    count = 0
    for i in range(1, son + 1):
        if son % i == 0:
            count += 1

    return count

def map_divisors_count(sequence):
    return map(divisors_count, sequence)

print(list(map_divisors_count([-8, 10, 4, 0, 12, -5])))
