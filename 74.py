def even_index_or_value(list):
    new_list = []
    for index in range(len(list)):
        if index % 2 == 0 or list[index] % 2 == 0:
            new_list.append(list[index])

    return new_list

print(even_index_or_value([1, 3, 2, 5, 7, 5]))