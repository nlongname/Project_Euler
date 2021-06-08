# https://projecteuler.net/problem=75
# Find out how many integer lengths of wire, L <= 1,500,000 can be bent
# into exactly one right triangle.
import math

def find_single_lengths(L:int, verbose=False) -> int:
    count = 0
    singles = set()
    multiples = set()
    # using a variant of Euclid's formula for generating Pythagorean triples
    # https://en.wikipedia.org/wiki/Pythagorean_triple#A_variant
    # if m and n are two odd integers with m > n
    # a = m*n, b = (m^2 - n^2)/2, and c = (m^2 + n^2)/2
    # if m and n are coprime, these each generate a unique "primitive" triple
    # (meaning a, b, and c are coprime), but we can multiply each by any k
    # to get others e.g. m=3 and n=1 generates (3,4,5),
    # we can multiply by various k to get (6,8,10), (9,12,15), etc.
    for m in range(1,int(L**(1/2)),2):
        for n in filter(lambda x: math.gcd(x,m) == 1,range(1,m,2)):
            length = m*(m+n)
            # this comes from adding our formulas for a,b,c
            # b+c = m^2, a+b+c = mn + m^2 = m(m+n)
            mult = L//length
            if mult == 0:
                break
            if verbose:
                print(m*n, int((m**2-n**2)/2), int((m**2+n**2)/2))
            for temp in range(length, length*mult+1, length):
                if temp in multiples:
                    next
                elif temp in singles:
                    singles.remove(temp)
                    multiples.add(temp)
                else:
                    singles.add(temp)
    if verbose:
        print(singles)
        print(multiples)
    return len(singles)

print(find_single_lengths(15*10**5))
