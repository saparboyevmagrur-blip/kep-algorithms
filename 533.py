def filter(func, sequence):
    lst = []
    for i in sequence:
        # lst.append(func(i)) # map
        if func(i):
            lst.append(i)

    return lst

print(filter(lambda x: x % 2 == 1, [1, 2, 3, 4]))