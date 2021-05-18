# https://projecteuler.net/problem=179
# Find the number of integers 1 < n < 10^7 where n and n+1 have the same
# number of positive divisors. e.g. 14 has 1,2,7,14 and 15 has 1,3,5,15

import math

def num_divisors(n:int):
    count = 0
    limit = math.sqrt(n)
    if int(limit) == limit: #if it's a perfect square that throws off the logic a little
        count += 1
    limit = math.ceil((limit))
    for i in range(1,limit):
        if n % i == 0:
            count += 2
    return count

total = 0
last = num_divisors(2)
for i in range(2,10**7+1):
    temp = num_divisors(i)
    if temp == last:
        #print((i-1, i))
        total += 1
    last = temp
    if i % 10**5 == 0:
        print(i)
#l = [num_divisors(n) for n in range(2,10**7+1)]
#successes = [l[i] == l[i+1] for i in range(len(l)-1)]
