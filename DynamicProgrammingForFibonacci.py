"""
this method is nor a dynamic programming method, it is waste of time and memory!
def fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
num = fib(40)
print(num)
"""

#dynamic programming method
def fib(n):
    f1 = 1
    f2 = 1
    for i in range(2, n+1):
        f = f1 + f2
        f1 = f2
        f2 = f
    return f

num = fib(40)
print(num)