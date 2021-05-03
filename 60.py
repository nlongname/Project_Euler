import math

with open('primes.txt', 'r') as filehandle:
    primes = [int(current_prime.rstrip()) for current_prime in filehandle.readlines()]

def prime_test(n:int):
    if n in primes:
        return True
    elif n > primes[-1]:
        for_now = True
        i = 0
        while for_now and primes[i]<=math.sqrt(n):
            if n % primes[i] == 0:
                for_now = False
            i += 1
        return for_now
    else:
        return False

def find_concatenators(so_far:list=[], l:int=5, pool:list=primes):
    banned = [2, 5]#, 109, 229, 541, 673, 823, 1237]
    if len(so_far) != 0:
        last = so_far[-1]
    else:
        last = 0
    for p in filter(lambda x: x > last and x not in banned, pool):
        if pool.index(p) % 100 == 0:
            print(p, pool.index(p))
        i = 0
        working=True
        while working and i < len(so_far):
            s = so_far[i]
            tests = [int(str(s)+str(p)), int(str(p)+str(s))]
            if prime_test(tests[0]) and prime_test(tests[1]):
                working=True
            else:
                working = False
                break
            i += 1
        if working:
            so_far.append(p)
            print(so_far)
            if len(so_far) == l:
                return so_far
            else:
                return find_concatenators(so_far, l, pool)
    return find_concatenators(so_far[:-1], l, list(filter(lambda x: 10000 > x > so_far[-1], primes)))
#print(sum(find_concatenators([],5,list(filter(lambda x: x< 10000, primes)))))

def check_pair(a:int, b:int):
    if prime_test(int(str(a)+str(b))) and prime_test(int(str(b)+str(a))):
        return True
    else:
        return False
results={}
i=0
to_check = [3]
while i < len(to_check):
    p = to_check[i]
    d = int(math.log(p,10))+1
    temp = filter(lambda x: x%(10**d)==p and int(x/(10**d)) in primes, primes)#finding #'s where right side works
    temp = map(lambda x: int(x/(10**d)), temp)
    temp = filter(lambda x: int(str(p)+str(x)) in primes, temp)
    temp = list(temp)
    if len(temp) >= 4:
        results[p] = list(temp)
        print((p, results[p]))
    for c in results[p]:
        if c not in to_check:
            to_check.append(c)
#    to_check = list(dict.fromkeys(to_check))
    i += 1
