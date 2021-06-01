# https://projecteuler.net/problem=381
# for a prime p, let S(p) = (p-1)! + (p-2)! + (p-3)! + (p-4)! + (p-5)!
# find the sum of S(p) for 5 <= p < 10^8
import math
import sympy

def frac_mod(n:int, d:int, p:int): #recycled from another problem
    #print(n,d,p)

    #default to regular division if you can
    n %= p
    d %= p
    if d==0:
        raise Exception("Undefined")
    check = n/d
    if int(check) == check:
        return int(check)
    if d==0 or p%d == 0:
        raise Exception("Undefined")
    # n/d = x mod p means dx = n (mod p) so if we multiply both sides by d
    # we should get dx = p*(something)+n take that mod d instead
    # 0 = p*multiplier + n (mod d) or p*multiplier = -n (mod d)
    # so if we know p mod d, that multiplier is -n/p (mod d)
    # this will always be smaller numbers, and often just be regular division
    multiplier = frac_mod(-n, p, d)
    return int((p*multiplier+n)/d)

def S(p:int) -> int:
    #(p-1)! is always -1 == p-1 mod p (assuming p's a prime, which I am)
    # so (p-2)! is 1 mod p, meaning the first two always cancel out
    # (p-3)! is 1/-2 = -1/2 mod p
    # (p-4)! is 1/-3 = -1/3 of (p-3)! = -1/3 * -1/2 = 1/6 mod p
    # and (p-5)! is 1/-4 = -1/4 of (p-4)! = -1/4 * 1/6 = -1/24 mod p
    # -1/24 + 1/6 - 1/2 = -9/24 (mod p or not)
    return frac_mod(-9,24,p)

def sum_S(limit:int = 10**8) -> int:
    result = 0
    for p in sympy.primerange(5,limit+1):
        result += S(p)
    return result
print(sum_S())
# not fast, but it works:
# 139602943319822
