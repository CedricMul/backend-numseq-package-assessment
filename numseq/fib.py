def fib(n):
    fibo = [0,1]
    a = 0
    b = 1
    if n <= 1:
        return fibo[n]
    else:
        while len(fibo) <= n:
            """Adding the previous 2 and updating them to new numbers"""
            c = a + b
            a = b
            b = c
            fibo.append(c)
        return fibo[n]

