mod = 1000000007

import functools

def power_mod_naive(base:int, exp:int, m:int=mod):
    result = 1
    for i in range(exp):
        result *= base
        result %= m
    return result

def power_mod(base:int, exp:int, m:int=mod):
    if exp == 0:
        return 1
    # to make this faster, we'll use a binary method
    # first, write the exponent in binary (lowest power on left)
    b = []
    while exp > 0:
        b.append(exp%2)
        exp = int(exp/2)
    powers = [base]
    for i in b[1:]:
        temp = powers[-1]**2 #find all the binary powers
        temp %= m
        powers.append(temp)
    result = [b[i]*powers[i] for i in range(len(b)) if b[i] != 0] #drop the ones with zeroes
    result = functools.reduce(lambda x, y: x*y%m, result)
    return result
        
        
def s_naive(n:int):
    return ((n%9+1)*10**int(n/9) - 1)%mod

def s(n:int):
    return ((n%9+1)*power_mod(10,int(n/9)) - 1)%mod

def s_sum_naive(n:int):
    return sum(map(s, range(1,n+1)))%mod

def s_sum(x:int):
    #core concept: for each multiple of 9, we're adding together a bunch of numbers followed by a list of 9's
    # e.g.: 19+29+39+49+59+69+79+89+99 for 10 <= x <= 18
    # this is 20+30+...+100 - 9 = 54*10 - 9
    # more generally: 54*10^n - 9 for the sum of 9n+1 to 9(n+1)
    # to get the full sum from 1 to 9(n+1), we're adding 54*(1+10+100+...) - 9n = 54*(111...) - 9n where 111... has n 1's
    # 111... is more easily calculated as (10^n - 1)/9 e.g. 111 = (10^3-1)/9 = 999/9 = 111
    # so 54 * (10^n - 1) / 9 - 9n simplifies to 6*(10^n - 1) - 9n as the sum for the first 9n numbers
    # 10^n is obviously going to get way too big, so we'll modulo that first then calculate the rest
    # usually we'll have a few leftover (our number isn't divisible by 9), and just do those using s for now
    n = int(x/9)
    remainder = x % 9
    result = 6*(power_mod(10,n,mod) - 1) - 9*n
    for i in range(remainder):
        result += s(x-i)
    return result%mod
    

def fib_list(n):
    count = 1
    result = [0, 1]
    while count < n:
        result.append(result[-1]+result[-2])
        count += 1
    return result

#sums = [s_sum(x)%1000000007 for x in fib_list(90)[2:]]
#print(sum(sums))

#frustratingly, this is super fast,
#matches with the slower versions and the example,
#but does not produce the right result
#haven't figured out why yet
f = fib_list(90)
total = 0
for i in range(2,91):
    temp = s_sum(f[i])
    total += temp
    total %= mod
    print(i, f[i], temp, total)

for i in f:
    a = s_sum_naive(i)
    b = s_sum(i)
    if a != b:
        print(i, a, b)
    else:
        print(i)
