#O(n^2)
def func(inp):
    for i in inp:
        for j in inp:
            print(i)
            print(9)
    
    for i in inp:
        print(9)
    
    #ทำงาน 100000000000 บรรทัด
        
#O(1)
def func2(inp):
    #ทำงาน 8 บรรทัด
    pass
    
#N คือความยาวของ input
# func([1, 4, 5, 5, 7])

#Recursion
def recur():
    print(1)
    recur()

#O(n)
def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)
   
recur_factorial(5)
5 * recur_factorial(4)
5 * 4 * recur_factorial(3)
5 * 4 * 3 * recur_factorial(2)
5 * 4 * 3 * 2 * recur_factorial(1)

5 * 4 * 3 * 2 * 1
