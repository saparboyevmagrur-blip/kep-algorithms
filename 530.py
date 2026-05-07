# implement
def map(func, sequence):
    lst = []
    for i in sequence:
        lst.append(func(i))

    return lst

# map(func, iterable)
# map(lambda x: x ** 2, sequence)
print(map(lambda x: x ** 2, [5, 0, -2]))
print(map(lambda x: x // 2, [1, 2, 3, 4]))