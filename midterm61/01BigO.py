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