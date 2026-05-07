# filter(func, iterable)
def filter_odd(sequence):
    return filter(lambda x : x % 2 == 0, sequence)

print(list(filter_odd([-5, 0, 8, 15, 12])))