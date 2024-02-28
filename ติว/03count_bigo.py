def func_raw(n):
    i = 1
    while i <= n:
        for j in range(0, i):
            print("x")
        i *= 2

def func(n):
    i = 1
    while i <= n:
        count = 1
        for j in range(0, i):
            print(f"{count} ", end = "")
            count += 1
        i *= 2
        print()

# func(16)
func_raw(4)
