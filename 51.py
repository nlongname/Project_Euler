import math
primes = []
with open('primes.txt', 'r') as filehandle:
    primes = [int(current_prime.rstrip()) for current_prime in filehandle.readlines()]

def sieve(limit=1000, already=[]):
    offset = 0
    if already != []:
        offset = already[-1]
        if limit < offset:
            return already
        else:
            nums = already + list(range(offset,limit))
    else:
        nums = list(range(2,limit))
    i = 0
    maximum = math.sqrt(limit)
    while i < math.sqrt(len(nums)) and nums[i] < maximum:
        n = nums[i]
        t = n*n #skip straight to the first multiple that's left
        if offset > t:
            t = (int(offset/n)+1)*n #pick the first multiple that wasn't pre-provided
        while t < limit:
            if t in nums:
                nums.pop(nums.index(t))
            t += n
        i += 1
    #print(nums[-1])
    with open('primes.txt', 'w') as filehandle:
        filehandle.writelines(str(p)+'\n' for p in nums)
    return(nums)

def more_primes(primes):
    print("moar")
    return(sieve(primes[-1]+25000, primes))

def prime_check(n, primes):
    i=0
    p=primes[i]
    limit = math.sqrt(n)
    while p < limit:
        if n % p == 0:
            return((False, primes))
        i += 1
        while len(primes)<i:
            primes = more_primes(primes)
        p = primes[i]
    return((True, primes))
    

def prime_replacements(streak_len = 8, primes=primes):
    min_digit = 10-streak_len
    useful_digits = [n for n in range(10) if n <= min_digit]
    print(useful_digits)
    ignore_list = []
    primes = sieve(10000,primes)
    i=1
    while True:
        p = primes[i]
        if p == primes[-1]:
            primes = more_primes(primes)
            print(primes[-1])
        #if p in ignore_list:
        #    ignore_list.remove(p)
        else:
            s = str(p)
            for ud in useful_digits:
                if str(ud) in s:
                    hits = [p]
                    misses = ud #i.e. if the digit is 2, we've apparently missed 0 and 1
                    while misses <= useful_digits[-1]-ud:
                        for n in range(ud+1,10):
                            test = int(s.replace(str(ud),str(n)))
                            #while test > primes[-1]:
                            #    primes = sieve(primes[-1]+1000,primes)
                            (flag, primes) = prime_check(test, primes)
                            if flag:
                                hits.append(test)
                            else:
                                misses += 1
                    if len(hits) >= streak_len:
                        print(hits)
                        return((hits, primes))
                    #else:
                    #    ignore_list += hits[1:]
        i += 1
        


(ans, primes) = prime_replacements(8)

with open('primes.txt', 'w') as filehandle:
    filehandle.writelines(str(p)+'\n' for p in primes)

