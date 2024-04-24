BKK_SOL: list[int] = [8500, 9000, 10000, 12000]
SOL_NYC: list[int] = [12500, 14000, 15000]

'''
วิธีทำให้ออกมาแบบในโจทย์
'''
price_list1: list[int] = []

for i in BKK_SOL:
    for j in SOL_NYC:
        price_list1.append(i+j)
price_list1.sort()
#print(price_list1) # -> [21000, 21500, 22500, 22500, 23000, 23500, 24000, 24000, 24500, 25000, 26000, 27000]

'''
ไม่เข้าใจโจทย์โมเม้น :(
'''