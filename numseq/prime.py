from math import sqrt

def is_prime(m):
    if (m <= 1):
        return False
    if (m == 2):
        return True
    """divisible by two?"""
    if (m % 2 == 0):
        return False

    i = 3
    """Divisible by any number less than the given?"""
    while i <= sqrt(m):
        if m % i == 0:
            return False
        i += 2

    return True

def primes(n):
    p_list = [2]
    x = 2
    """Runs through numbers adding primes until it reaches n"""
    while p_list[-1] < n:
        x += 1
        if is_prime(x):
            p_list.append(x)
    if p_list[-1] > n:
        p_list.pop()
    return p_list
