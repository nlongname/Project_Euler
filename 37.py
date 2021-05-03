import math, itertools

def sieve(limit=1000000, already=[]):
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

def truncatable_primes(limit):
    already_checked = int(limit/10)
    const = sieve(already_checked)
    max_length = math.ceil(math.log(limit-1,10))
    candidates = []
    prime_candidates = []
    rtol=[]
    final=[]
    for l in range(2,max_length+1): 
        possible_digits = [1,3,7,9]
        digits_list = [possible_digits]*l #making a list of possible digits for each slot
        digits_list[0] += [2,5] #can only have 2 or 5 if it ends up being a prime by itself
        digits_list[0].sort()
        pre_candidates = list(itertools.product(*digits_list)) #finding all combinations through list comprehensions
        new_candidates = map(process_candidate, pre_candidates) #turning them back into regular numbers
        candidates += new_candidates #adding them to the list of candidates
    #print(len(candidates))
    for c in candidates: #checking the candidates we've found for primality
        if c < already_checked and c in const:
            prime_candidates.append(c)
        elif c >= already_checked:
            prime = True
            ceiling = math.sqrt(c)
            i=0
            while prime and i < len(const) and const[i] < ceiling:
                if  c % const[i] == 0:
                    prime = False
                i += 1
            if prime and c < limit: #unlikely, but in case of a very small limit
                prime_candidates.append(c)
    #print(prime_candidates)
    prime_candidates.reverse()
    for p in prime_candidates:
        if p not in rtol: #only going one direction, not both
            chain = []
            while p > 0:
                chain.append(p)
                p = int(p/10)
            #print(chain)
            chain_works = True
            for c in chain:
                if c not in const and c not in prime_candidates:
                    chain_works = False
            if chain_works:
                #print(chain)
                rtol += chain[:-1]
    rtol.sort()
    for p in rtol:
        if p not in final: #only going one direction, not both
            chain = []
            temp = str(p)
            while len(temp) > 0:
                chain.append(int(temp))
                temp = temp[1:]
            #print(chain)
            chain_works = True
            for c in chain:
                if c not in const and c not in rtol:
                    chain_works = False
            if chain_works:
                print(chain)
                final.append(chain[0])
    final.sort()
    print(final)
    if len(final) == 11:
        print(sum(final))
                   
                
                
        
def process_candidate(digits):
    n=0
    while len(digits)>0:
       n *= 10
       n += digits[0]
       digits = digits[1:]
    return(n)

truncatable_primes(1000000)
