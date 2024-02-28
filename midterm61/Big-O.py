#1.1
def q1(n):
    i = 0
    while i < n:
        j = 0
        while j < i:
            print(1)
            j += 1
        i += 1

q1(5)
'''
i j
0 
1 0
2 0 1
3 0 1 2
4 0 1 2 3

total runtime => (1/2)n^2
O(n^2)
'''

#1.2
def q2(n):
    i = 1
    while i < n:
        j = 0
        while j < i:
            print(1)
            j += 1
        i *= 2

q2(17)
'''
i  j
1  0                                        -- n/16
2  0 1                                      -- n/8
4  0 1 2 3                                  -- n/4
8  0 1 2 3 4 5 6 7                          -- n/2
16 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15    -- n

total runtime => 2n
O(n)
'''

#1.3
def q3(n):
    i = n
    while i > 1:
        j = 0
        while j < i:
            print(1)
            j += 1
        i /= 2

q3(16)
'''
i  j
16 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15    -- n
8  0 1 2 3 4 5 6 7                          -- n/2
4  0 1 2 3                                  -- n/4
2  0 1                                      -- n/8

total runtime => 2n
O(n)
'''