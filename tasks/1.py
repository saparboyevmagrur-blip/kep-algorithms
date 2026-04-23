# lst = [18, 22, 5, 38, 0, 7]
# print(7 in lst)
# 1-usul
# def month_to_season(month):
#     if month == 12 or 1 <= month <= 2:
#         return 'Qish'
#     elif 3 <= month <= 5:
#         return 'Bahor'
#     elif 6 <= month <= 8:
#         return 'Yoz'
#     elif 9 <= month < 12:
#         return 'Kuz'
# 2-usul:    
def month_to_season(month):
    if month in [12, 1, 2]:
        return 'Qish'
    elif month in [3, 4, 5]:
        return 'Bahor'
    elif month in [6, 7, 8]:
        return 'Yoz'
    elif month in [9, 10, 11]:
        return 'Kuz'
print(month_to_season(5))
print(month_to_season(12))