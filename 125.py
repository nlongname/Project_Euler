# https://projecteuler.net/problem=125
# Find the sum of all the numbers less than 10^8 that are both palindromic
# and can be written as the sum of consecutive squares.
# e.g. 6^2 + 7^2 + 8^2 + 9^2 + 10^2 + 11^2 + 12^2 = 595

import math

def is_palindrome(n:int):
    n = str(n)
    check_len = int(len(n)/2) # not super obvious, but this works for one-digit numbers also
    return n[:check_len] == n[:-check_len-1:-1]

def palindromic_sums(limit:int = 10**8):
    cutoff = int(math.sqrt(limit/2))
    square_sums = [int((2*n+1)*n*(n+1)/6) for n in range(1,cutoff+1)] # sum of squares from 1 to n is (2n+1)(n)(n+1)/2, similar to the triangular number formula
    pal_square_sums = [s for s in square_sums[1:] if is_palindrome(s)] # excludes 1, which isn't a "sum"
    pal_square_sums = [s for s in pal_square_sums if s < limit]
    for i in range(len(square_sums)):
        if i > 1:
            for j in range(len(square_sums[:i-1])): # make sure you're not subtracting neighbors and getting just 1 square number
                temp = square_sums[i]-square_sums[j]
                if temp < limit and is_palindrome(temp):
                    pal_square_sums.append(temp)
                    #print(i+1, j+1, temp)
    result = sum(set(pal_square_sums)) # remove duplicates
    return result

print(palindromic_sums())
