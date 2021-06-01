# https://projecteuler.net/problem=203
# Find the sum of the distinct squarefree numbers in the first 51 rows
# of Pascal's triangle.
# A "squarefree" number is one not divisible by the square of any prime.

# Pascal's triangle can be calculated by the binomial coefficient
# here math.comb(n,k) = n! / (k! * (n-k)!)
# Because of the factorials, the only primes that could be squared are those
# p <= n/2, so that another copy of that prime would get multiplied in at 2p
# (still might not work depending on the numerator, but that's as far as we need)

import math
import sympy

def squarefree_binomials(num_rows:int) -> int:
    sq_free_sum = 0
    prime_squares = [p**2 for p in sympy.primerange(1,num_rows/2+1)]
    distinct = set()
    for n in range(num_rows):
        for k in range(int(n/2+1)):
            b = math.comb(n,k)
            sq_free = True
            if b not in distinct:
                for p_sq in prime_squares:
                    if b%p_sq == 0:
                        sq_free = False
                        break
                if sq_free:
                    sq_free_sum += b
                #else:
                #    print(n, k, b)
                distinct.add(b)
    return sq_free_sum
