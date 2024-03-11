from math import sqrt

#Big O
def q1(n):
    i = 1
    while 1 < n:
        for i in range(0, n):
            print("x")
        i *= 2

def q2(n):
    i = 1
    while 1 < n:
        for i in range(0, i):
            print("x")
        i *= 2
    
def q4(n):
    for i in range(0, sqrt(n)):
        print("x")
    
    q4(n/4)
    q4(n/4)

def q5(n):
    if n == 0:
        return
    
    print("x")
    q5(n - 1)

def q6(n):
    if n == 0:
        print("x")
    
    for i in range(0, n):
        q6(n)

#2
'''
ให้ class LinkedList มาแบบแหว่ง จงเติมให้เต็ม
(insert append prepend ...)
ที่สำคัญคือ reverse
'''

#3
'''
ก --- ทำ sequential search
ข --- ทำ sort และ binary search

ถ้า list(ความยาว n) ไม่ได้เรียงมา จงวิเคราะห์ว่าแบบไหนเร็วกว่า
1) สำหรับการทำครั้งเดียว
2) สำหรับการทำ n ครั้ง(เท่ากับจำนวนของใน list)
'''

#4
#queue จาก 2 stack

#5
#เศรษฐากับถุงเท้า

#6
#แถวซื้อของ