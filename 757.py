# https://projecteuler.net/problem=757
# A positive integer N is "stealthy" if there exist positive a,b,c,d such
# that ab = cd and a+b = c+d+1. For example, 36 = 4x9 = 6x6 is stealthy
# How many stealthy numbers are there <= 10^14

# I set c=a-x, d=b+x-1, so ab = cd = x^2 + (b-a-1)x + a = 0, solve for x
# and the discriminant is (b-a-1)^2 - 4a, which needs to be a square number
# Set that equal to n^2 (so the square root of the discriminant is n) and
# you get b = a +/- sqrt(4a+n^2) + 1. I assumed b > a, so we use the +.
# if we try out n^2 - (n-m)^2 = 4a, this only works for even m, so let's call
# it n^2 - (n-2i)^2 = 4a and we get n = a/i + i, for all positive integers i

import math

# first try, straightforward approach
def find_stealthy(limit:int = 10**6):
    a_limit = int(math.sqrt(limit))
    results = set()
    #squares = [x**2 for x in range(a_limit+1)]
    for a in range(1,a_limit+1):
        #n_list = [i for i, n in enumerate(squares[:a+2]) if n >= 4*a and n-(4*a) in squares]
        n_list = [int(a/i)+i for i in range(1,int(math.sqrt(a)+1)) if a%i==0]
        #print(a, n_list)
        ab_list = [a*(a+n+1) for n in n_list]
        #ab_list += [a*(a-n+1) for n in n_list]
        ab_list = [ab for ab in ab_list if ab <= limit and ab > 0]
        if math.sqrt(a)%1== 0:
            print(a, n_list)
        results.update(ab_list)
    return len(results)

# It turns out to be easier if you flip it around, a = i(n-i) for positive
# integers n and i. b works out to a+n+i, then multiply a*b. I worked some
# quadratics to set maximum and minimum limits for n and i when needed, but mostly you
# iterate up until ab is too big.

def find_stealthy_faster(limit:int = 10**14):
    results = set()
    repeats = []
    count = 0
    removed = 0
    max_n = int(math.sqrt(1/4+limit/2)+1/2)
    for n in range(2,max_n+1):
        try:
            results.remove(n-2)
            removed += 1
        except:
            next
        temp = 0
        i = 1
        while temp < limit and i <= n/2:
            a = i*(n-i)
            b = a+n+1
            temp = a*b
            if temp <= limit:
                count += 1
                if temp in results:
                    if temp in repeats:
                        next
                        #print(n, a, b, temp)
                    repeats.append(temp)
                results.add(temp)
            else:
                break
            i += 1
    return removed+len(results)

def find_stealthy_limited(limit:int = 10**14, lower:int = 1):
    # had to break it down into smaller pieces to not run out of memory
    results = set()
    repeats = []
    count = 0
    max_n = int(math.sqrt(1/4+limit/2)+1/2)
    min_n = max(2,int(2*lower**(1/4)-1))
    for n in range(min_n,max_n+1):
        temp = 0
        i = 1
        if n==6:
            next
        while temp < limit and i <= n/2:
            a = i*(n-i)
            b = a+n+1
            temp = a*b
            if temp >= lower and temp <= limit:
                count += 1
                results.add(temp)
            i += 1
    return len(results)

l = []
for i in range(10):
    temp = find_stealthy_limited((i+1)*10**13,i*10**13)
    l.append(temp)
    #print(temp)
print(sum(l))
