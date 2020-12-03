import numpy as np


NORGE = 5_433_000


def isprime(n):
    if n == 2:
        return True
    if n & 1 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def largest_prime_below(n):
    for i in range(n):
        if isprime(n - i):
            return n - i
    return -1


pakker, ctr = 0, 0
while ctr < NORGE:
    if "7" in str(ctr):
        ctr += largest_prime_below(ctr)
    else:
        pakker += 1
    ctr += 1

print(f"Nissen leverte {pakker} pakker.")