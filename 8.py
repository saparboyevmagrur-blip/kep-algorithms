def reverse_number(number):
    string = str(number)
    return string[::-1]
n=input() # 123000 => '123000' => '000321'
count = 0
for i in reverse_number(n):
    if i == '0':
        count += 1
    else:
        break
    
print(count)
