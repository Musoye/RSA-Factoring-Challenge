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
    #print(is_prime(a + c))
    #print(is_prime(a - c))
    print("{:d}={:d}*{:d}".format(int(n), int(a + c), int(a - c)))

def start():
    """where to run the file"""
    import sys

    lis = sys.argv
    if len(lis) < 2:
        print("Error!: <USAGE> -> ./rsa filename")
        exit(98)
    f_name = ''
    if len(lis) == 2:
        f_name = lis[1]
    if len(lis) == 3:
        f_name = lis[2]
    with open(f_name ) as file_in:
        lines = []
        for line in file_in:
            lines.append(line);
    if len(lines) == 0:
        print("The file is empty")
        exit(98)
    is_rsa(int(lines[0]))
start()
