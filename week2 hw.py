#e = 0.001

def mystery(x, a, b):
    c = (a + b) / 2
    d = c**2 - x

    if abs(d) <= e:
        return c
    elif d > e:
        return mystery(x, a, c)
    else:
        return mystery(x, c, b)
    
#print(mystery(7, 2, 3))

# try to find time complexity (plz send help)

def mystery_debug(x, a, b, e, count = 0):
    c = (a + b) / 2
    d = c**2 - x
    count += 1

    if abs(d) <= e:
        return c, count
    elif d > e:
        return mystery_debug(x, a, c, e, count)
    else:
        return mystery_debug(x, c, b, e, count)
    
print(mystery_debug(3.999996185303644, 1, 2, 0.1))
print(mystery_debug(3.999996185303644, 1, 2, 0.01))
print(mystery_debug(3.999996185303644, 1, 2, 0.0001))

print(mystery_debug(2, 1, 2, 0.1))
print(mystery_debug(2, 1, 2, 0.01))
print(mystery_debug(2, 1, 2, 0.0001))
