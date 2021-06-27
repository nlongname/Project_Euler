# https://projecteuler.net/problem=387

# A Harshad number is one that is divisible by the sum of its digits

# If we can repeatedly cut off the last digit and still get a Harshad number
# then we call it a right-truncatable Hardshad number
# e.g. 201 (divisible by 3) -> 20 (divisible by 2) -> 2 (divisible by 2)

# When we divide a number n by its digit sum and get a prime we call that
# a "strong" Harshad number, e.g. 201/3 == 67 is strong because 67 is prime

# Finally, we define a "strong, right truncatable Harshad prime" to be a
# prime number that if you cut off the last digit, you get a strong Harshad
# number that is also truncatable, e.g. 2011 is prime -> 201 which we showed
# previously is strong and right-truncatable.

# We want the sum of all such primes < 10^14

import sympy, math

# General approach: build the chains up backwards, 2 -> 20 -> 201
# so 2 -> 20, 21, 24, 27
# while we're at it, we check if any of these are "strong"
# If so we need to check if any primes can be truncated to that "strong" number

def harshad_sum(l:int=10**14) -> int:
    exp = math.log(l,10)
    n=1
    current = list(range(1,10)) #initialize the chain with single digits (all are possible)
    strongs = []
    new = []
    while n < exp-1:
        for x in current:
            d_sum = sum(int(d) for d in str(x))
            new_x = x*10
            for i in range(10):
                if (new_x + i) % (d_sum + i) == 0: # check for Harshad-ness
                    new.append(new_x+i)
                    if sympy.isprime((new_x+i) // (d_sum + i)): # check for strength
                        strongs.append(new_x+i)
        n += 1
        current = new # maintain current to always be n-digit numbers
        new = []
    return sum(sum(p for p in sympy.primerange(x*10, x*10+10) if p < l) for x in strongs)
            # for each x (strong Harshad number) we find all the primes that
            # could be truncated to that, check if they're less than the limit
            # and sum those, then sum across all strong Harshads we found
