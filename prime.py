#!/usr/bin/python3
def is_prime(num):
    """Check if a number is prime
    using primilarity test"""
    import math
    i = 2
    while (i <= math.sqrt(num)):
        if (num % i == 0):
            return False
        i += 1
    return (True)
#print(is_prime(19))
#print(is_prime(21))
