def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)

def fibs(n):
    ls = []
    for i in range(1,n + 1):
        ls.append(fib(i))
    return ls

def isfib(n):
    a = 1
    while fib(a) <= n:
        if fib(a) == n:
            return True
        a += 1
    return False