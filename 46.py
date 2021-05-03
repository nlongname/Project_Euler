import math, itertools

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
    while i < len(nums) and nums[i] < math.sqrt(limit):
        n = nums[i]
        t = n*n #skip straight to the first multiple that's left
        if offset > t:
            t = (int(offset/n)+1)*n #pick the first multiple that wasn't pre-provided
        while t < limit:
            if t in nums:
                nums.pop(nums.index(t))
            t += n
        i += 1
    return(nums)

def goldbach_other():
    primes = []
    double_squares = []
    odd_composites = []
    combos = []
    old_limit = 1
    new_limit = 1000
    while True:
        for i in odd_composites:
            if i < old_limit and i not in combos:
                print(combos)
                print(i)
                return(i)
        #print(new_limit)
        primes = sieve(2*new_limit, primes)
        new_double_squares = [2*x**2 for x in range(math.ceil(math.sqrt(old_limit/2)),math.ceil(math.sqrt(new_limit/2))) if 2*x**2 <= new_limit]
        new_odd_composites = [2*x+1 for x in range(old_limit,new_limit) if ((2*x+1 not in primes) and x!=0)]
        double_squares += new_double_squares
        #print(old_limit, new_limit)
        odd_composites += new_odd_composites
        #print(double_squares)
        for d in new_double_squares:
            new_combos = [d+p for p in primes if d+p not in combos and d+p in odd_composites and old_limit < p < new_limit]
            combos += new_combos
            #print(combos)
        for p in primes:
            if old_limit < p < new_limit:
                new_combos = [d+p for d in double_squares if d+p not in combos and d+p in odd_composites]
                combos += new_combos
        #before = len(combos)
        #combos = list(dict.fromkeys(combos))
        combos.sort()
        #after = len(combos)
        #if after < before:
        #    print(f"yes, {before-after}")
        old_limit = new_limit
        new_limit = new_limit + 1000
        

def goldbach_new():
    primes = sieve(1000)
    double_squares = [2]
    dslen = 1 #length of double squares, i.e. the last number I squared and doubled
    odd_composite = 9
    while True:
        while double_squares[-1] < odd_composite:
            double_squares.append(double_squares[-1]+4*dslen + 2) #2n^2 + 4n+2 = 2(n+1)^2, keeps multiplication to smaller numbers
            dslen += 1
        while primes[-1] < odd_composite+2: #+2 to cover for the next one down below
            primes = sieve(primes[-1]+1000, primes)
        works = False
        for d in double_squares:
            if odd_composite - d in primes:
                works = True
        if not works: #we're specifically looking for something that /doesn't/ work
            print(odd_composite)
            return(odd_composite)
        odd_composite += 2
        while odd_composite < primes[-1] and odd_composite in primes:
            odd_composite += 2
            if odd_composite > primes[-1]:
                primes = sieve(primes[-1]+1000, primes)
        #if odd_composite % 1000 == 5:
        #    print(odd_composite)
        #    print(double_squares)


goldbach_new()
