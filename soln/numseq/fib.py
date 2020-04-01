def fib(n):
    z = n-1
    fibo = [0,1]
    a = 0
    b = 1
    if z <= 1:
        return fibo[z]
    else:
        while len(fibo) <= n:
            c = a + b
            a = b
            b = c
            fibo.append(c)
        return fibo[z]
            