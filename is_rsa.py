#!/usr/bin/python3
def is_sqr(num):
    """check if a number is squared"""
    import math

    a = int(math.sqrt(num))
    if (a * a == num):
        return (True)
    return (False)
def is_rsa(n):
    """split the rsa of a number"""
    import math
    from prime import is_prime

    a = int(math.sqrt(n)) + 1
    while True:
        b = a ** 2 - n
        if is_sqr(b):
            c = math.sqrt(b)
            break
        a = a + 1
    print(is_prime(a + c))
    print(is_prime(a - c))
    print("{:d}={:d}*{:d}".format(int(n), int(a + c), int(a - c)))
is_rsa(35)
