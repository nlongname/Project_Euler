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

def circular_primes(limit):
    already_checked = int(math.sqrt(limit))
    const = sieve(already_checked)
    possible_digits = [1,3,7,9] #anything including other digits will cycle to a multiple of 2 and/or 5
    max_length = math.ceil(math.log(limit-1,10))
    candidates = [2,3,5,7] #except for the one-digit prime numbers themselves
    prime_candidates = []
    final=[]
    for l in range(2,max_length+1): 
        digits_list = [possible_digits]*l #making a list of possible digits for each slot
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
    #print(len(prime_candidates))
    for p in prime_candidates:
        if p not in final:
            chain = []
            temp = str(p)
            while temp not in chain:
                chain.append(temp)
                temp = temp[-1]+temp[:-1]
            chain = list(map(int, chain))
            #print(chain)
            chain_works = True
            for c in chain:
                if c not in prime_candidates:
                    chain_works = False
            if chain_works:
                final += chain
    print(final)
    print(len(final))
                   
                
                
        
def process_candidate(digits):
    n=0
    while len(digits)>0:
       n *= 10
       n += digits[0]
       digits = digits[1:]
    return(n)

circular_primes(1000000)
