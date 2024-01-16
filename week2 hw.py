e = 0.1

def mystery(x, a, b):
    c = (a + b) / 2
    d = c**2 - x

    if abs(d) <= e:
        return c
    elif d > e:
        return mystery(x, a, c)
    else:
        return mystery(x, c, b)
    
print(mystery(1, 1, 1))