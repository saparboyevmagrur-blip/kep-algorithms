lst = [18, 22, 5, 38, 0, 7]
s = 0
for element in lst:
    if element < 30 and element % 3 == 0:
        print(element, end=" ")
    else:
        s += element # s = s + element

print()
print(s)

# for index in range(len(lst)):
#     print(index, lst[index])
