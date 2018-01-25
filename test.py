

def fac(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n * fac(n-1)


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)





def fib2(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b


for x in range(0, 10):
    print(fib(x))
