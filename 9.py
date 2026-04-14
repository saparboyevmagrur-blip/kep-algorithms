# stringni kesib olish va teskarisiga o'girish
# txt = 'abcd'
# print(txt[1 : 3]) # bc
# print(txt[0 : len(txt)]) # abcd
# print(txt[0::]) # abcd
# print(txt[::-1]) # dcba

def reverse_number(number):
    string_number = str(number)
    return int(string_number[::-1])
# print(reverse_number(1895)) # 5981

for num in range(1000, 10000):
    reverse_num = reverse_number(num)
    if reverse_num == 4 * num:
        print(num)
# 2178 * 4
# 8712