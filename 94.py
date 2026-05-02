# 1. raqamlar yig'indisini topuvchi funksiya
# 2. raqamlar ko'paytmasini topuvchi funksiya
# 3. 100, 1000 gacha bo'lgan sonlar kerak, 
# har bir sonni p / s ga qoldiqsiz bo'linadiganni chiqaring
def raqamlar_yigindisi_kopaytmasi(son):
    s, p = 0, 1 # son = 785 => "785" => "7", "8", "5"
    for raqam in str(son):
        s += int(raqam)
        p *= int(raqam)

    return s, p

for son in range(100, 1000):
    s, p = raqamlar_yigindisi_kopaytmasi(son)
    if p % s == 0:
        print(son)
