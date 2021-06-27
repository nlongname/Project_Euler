# https://projecteuler.net/problem=357
# Consider the divisors of 30: 1,2,3,5,6,10,15,30
# It can be seen that for every divisor d of 30, d + 30/d is prime

# Find the sum of all positive integers n < 100,000,000
# such that for every divisor d, d+n/d is prime

import math, sympy
from functools import lru_cache

def prime_divisor_pairs(n:int) -> bool:
    for i in range(1,int(math.sqrt(n))+1):
        if n%i == 0 and not isprime(i + n//i):
            return False
    return True

@lru_cache
def isprime(n:int) -> bool:
    return sympy.isprime(n)

def prime_generating_integers(l:int=10**8) -> int:
    return sum(p-1 for p in sympy.primerange(1,l) if prime_divisor_pairs(p-1))
# since every number is divisible by 1, 1+n always has to be prime
# this also means that n is always divisible by 2 (except for 1)
# so n/2 + 2 is also always prime
# I'm not using that fact, but I wonder if it could maybe help speed this up

prime_generating_integers()
