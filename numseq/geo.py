def square(n):
    """Just square it, dawg"""
    n = n + 1
    return n * n

def triangle(n):
    adder = 2
    start = 1
    x = 0
    """Every addition, the adder gets +1 simulating the next layer"""
    for i in range(n):
        x = start
        start += adder
        adder += 1
    return x

def cube(n):
    """Cubed"""
    x = n + 1
    return x * x * x
