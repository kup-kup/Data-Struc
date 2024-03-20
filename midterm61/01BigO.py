from math import sqrt

#หา Time Complexity (BigO) ของฟังก์ชันต่อไปนี้ โดยคำนวณตามครั้งที่ print(x) ทำงาน
#โจทย์มาอะไรประมาณนี้

#1
#ในโจทย์
def q1(n):
    i = 1
    while i < n:
        for j in range(0, n):
            print("x")
        i *= 2

#ปรับ
def q1_mod(n):
    count = 0

    i = 1
    while i < n:
        for j in range(0, n):
            print(j, end = " ")
            count += 1
        print()
        i *= 2
    
    print(f"q1: {count}")

#q1_mod(17)
'''
n = 17
output:
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16

ทำงาน (n)log(n) ครั้ง
q1: O(n * log(n))
'''

#2
#ในโจทย์
def q2(n):
    i = 1
    while i < n:
        for j in range(0, i):
            print("x")
        i *= 2

#ปรับ
def q2_mod(n):
    count = 0

    i = 1
    while i < n:
        for j in range(0, i):
            print(j, end = " ")
            count += 1
        print()
        i *= 2

#q2_mod(17)
'''
n = 17
output:
0                                       --- n / 16
0 1                                     --- n / 8
0 1 2 3                                 --- n / 4
0 1 2 3 4 5 6 7                         --- n / 2
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15   --- n

ทำงาน 2n ครั้ง
q2: O(n)
'''
#3
#ลืม หายไปตามกาลเวลา :(

#4
#ในโจทย์
def q4(n):
    for i in range(0, sqrt(n)):
        print("x")
    
    q4(n/4)
    q4(n/4)

#ปรับ
def q4_mod(n):
    for i in range(0, int(sqrt(n))):
        print(i, end = " ")
    print()

    if n > 4:
        q4_mod(n/4)
        q4_mod(n/4)

#q4_mod(256) #256 = 4 ^ 4 
'''
n = 256
output:
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 --- sqrt(n)
0 1 2 3 4 5 6 7                       --- sqrt(n/4)
0 1 2 3                               --- sqrt(n/4**2)
0 1                                   --- sqrt(n/4**3)
0 1                                   --- sqrt(n/4**3)
0 1 2 3                               --- sqrt(n/4**2)
0 1                                   --- sqrt(n/4**3)
0 1                                   --- sqrt(n/4**3)
0 1 2 3 4 5 6 7                       --- sqrt(n/4)
0 1 2 3                               --- sqrt(n/4**2)
0 1                                   --- sqrt(n/4**3)
0 1                                   --- sqrt(n/4**3)
0 1 2 3                               --- sqrt(n/4**2)
0 1                                   --- sqrt(n/4**3)
0 1                                   --- sqrt(n/4**3)


n = 256
                     q4(256)                        --- ชั้นที่ 1: sqrt(n)
            /                      \ 
        q4(64)                     q4(64)           --- ชั้นที่ 2: 2sqrt(n/4)  = sqrt(n)
      /        \                 /        \ 
  q4(16)       q4(16)       q4(16)       q4(16)     --- ชั้นที่ 3: 4sqrt(n/16) = sqrt(n)
  /    \       /    \       /    \       /    \ 
q4(4) q4(4)  q4(4) q4(4)  q4(4) q4(4)  q4(4) q4(4)  --- ชั้นที่ 4: 8sqrt(n/64) = sqrt(n)

จำนวนชั้นที่ทำงานมาจาก log(256) ฐาน 4 = 4 ชั้น
ทำงานทั้งหมด sqrt(n)log(n) ครั้ง

q4: O(sqrt(n)log(n))
'''

#5
#ในโจทย์
def q5(n):
    if n == 0:
        return
    
    print("x")
    q5(n - 1)

#ปรับ
def q5_mod(n, count = 0):
    if n == 0:
        print(f"q5: {count}")
        return
    
    print(count)
    q5_mod(n - 1, count + 1)

q5_mod(7)
'''
n = 7
output:
0
1
2
3
4
5
6
q5: 7

ทำงาน n ครั้ง
q5: O(n)
'''

#6
#ในโจทย์
def q6(n):
    if n == 0:
        print("x")
    
    for i in range(0, n):
        q6(i)

#ปรับ
def q6_mod(n):
    if n == 0:
        print("x")
    
    for i in range(0, n):
        print(i, end = " ")
        q6_mod(i)

q6_mod(5)
'''
n = 4
output:
0 x
1 0 x
2 0 x
1 0 x
3 0 x
1 0 x
2 0 x
1 0 x

ให้ q6(n) ทำงาน T(n) ครั้ง
ได้ว่า 
n   T(n)
1   1          
2   2          = 2 * T(1)
3   4          = 2 * T(2)
4   8          = 2 * T(3)
5   16         = 2 * T(4)
           ...
n   2^(n-1)    = 2 * T(n-1)

ทำงาน 2^(n-1) ครั้ง
q6: O(2^n)
'''