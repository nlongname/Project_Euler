# https://projecteuler.net/problem=504
# Let ABCD be a quadrilateral whose vertices are lattice points lying on the
# coordinate axes as follows: A=(a,0), B=(0,b), C=(-c,0), D=(0,-d) where
# 1 <= a,b,c,d <= m and a,b,c,d,m are all integers

# How many quadrilaterals ABCD, for m=100 contain a square number of
# lattice points in their interior (not on the boundaries)?

from functools import lru_cache,reduce
from decimal import Decimal
import math

# by Pick's theorem, A = i + b/2 - 1, where i is the number of
# "internal" lattice points and b is the "boundary" lattice points
# so we can rearrange to i = A - b/2 + 1, and each of these is easier
# to calculate directly than i
# to avoid rounding issues, let's do i = (2A-b+2)/2

@lru_cache
def gcd(a,b):
    return math.gcd(a,b)

@lru_cache
def quad_lattice(a:int,b:int,c:int,d:int)->int:
    double_A=(a*b+b*c+c*d+d*a)
    b = gcd(a,b)+gcd(b,c)+gcd(c,d)+gcd(d,a)
    return (double_A-b+2)//2

def square_quad_lattice(m:int) -> int:
    count = 0
    other_count = 0
    for i in range(1,m+1):
        for j in range(1,m+1):
            for k in range(1,m+1):
                for l in range(1,m+1): #obviously this is ugly and takes longer than I'd like, but the symmetries are pretty complicated
                    p = quad_lattice(i,j,k,l)
                    if int(math.sqrt(p))**2 == p:
                        count += 1
                    other_count += 1
    #if other_count%(10**6):
    #    print(other_count)
    return count
square_quad_lattice(100)
