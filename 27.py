verbose = False

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
    for n in nums:
        t = 2*n #skip first multiple, itself
        if offset > t:
            t = (int(offset/n)+1)*n #pick the first multiple that wasn't pre-provided
        while t < limit:
            if t in nums:
                nums.pop(nums.index(t))
            t += n
    return(nums)
const = sieve(1000)
check = const

best_a = 0
best_b = 0
score = 0
for b in const: #b has to be prime so that n==0 works
    linear = map(lambda x: x-b-1, const) #narrowing field more by ensuring n==1 works
    temp_score = 0
    temp_best = 0
    for a in linear:
        flag = True
        n=2 #since we narrowed before, we can skip straight to n=2
        while flag:
            test = n*n + n*a + b
            if test > check[-1]: #make our pool of primes bigger if needed
                new_limit = check[-1]+1000
                #print(new_limit)
                check = sieve(new_limit,check)
            if test in check:
                n += 1
            else:
                 if n-1 > temp_score:
                     temp_best = a
                     temp_score = n-1
                 flag=False
    #print("Best for b=="+str(b)+" is "+str(temp_best)+" with a score of "+str(temp_score))
    if temp_score > score:
        best_b = b
        best_a = temp_best
        score = temp_score
        if verbose:
            print("best so far is b=="+str(best_b)+" and a=="+str(best_a)+" with "+str(score))
print("best is b=="+str(best_b)+" and a=="+str(best_a)+" with "+str(score))
print(best_b * best_a)
