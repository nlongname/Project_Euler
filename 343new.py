import math, time

primes = []
with open('primes.txt', 'r') as filehandle:
    primes = [int(current_prime.rstrip()) for current_prime in filehandle.readlines()]

def prime_check(n):
    if n in primes:
        return True
    i=0
    p=primes[i]
    limit = math.sqrt(n)
    if primes[-1] < limit:
        print("not enough primes")
    while p <= limit:
        if n % p == 0:
            return(False)
        i += 1
#        while len(primes)<i:
#            primes = more_primes(primes)
        p = primes[i]
    return(True)

def prime_div(n):
    if n in [0, 1]:
        return n
    if n in primes:
        return n
    i=0
    p=primes[i]
    limit = math.sqrt(n)
    while p <= limit:
        if n % p == 0:
            return p
        i += 1
        p = primes[i]
    return n

def frac(i:int, j=None):
    if type(i) == tuple:
        return(i)
    if j != None:
        return(i, j)
    else:
        return((i, 1))

def lcm(x:int, y:int):
    return(int(x*y/gcf(x,y)))

def gcf(x:int, y:int):
    b = max(x, y)
    s = min(x, y)
    while s != 0:
        b = b-s*(int(b/s))
        temp = b
        b = s
        s = temp
    return(b)

def simp(a:tuple or int, b=None):
    if b != None:
        a = (a, b)
    if type(a)==int:
        return(frac(a))
    else:
        g = gcf(a[0],a[1])
        n = int(a[0]/g)
        d = int(a[1]/g)
        return((n,d))

record = {}

max_log = [0]
def seq(k:int):
    #if k in record.keys():
    #    print(f"repeat: {k}")
    #    return record[k]
    f = (1, k)
    #recordable=[k]
    #num_limit = round(k**(1/3)+1)
    while f[1] != 1:
        f = (f[0]+1, f[1]-1)
        #if f[0] == 1:
        #   if f[1] in record:
        #       print(f"repeat: {f[1]}")
        #       for r in recordable:
        #           if r not in record.keys():
        #               record[r] = record[f[1]]
        #       return(record[f[1]])
        #   recordable.append(f[1])
        if f[1] == 1:
            return f[0]
        if f[1]%f[0] == 0:
            #log = f[0]
            #if log > max_log[-1]:
            #    max_log.append(log)
            #    print(f, max_log[-1])
            #print(log)
            f = (1, int(f[1]/f[0]))
            if prime_check(sum(f)):
                return(f[1])
        elif f[0] > f[1]:
        #   for r in recordable:
        #       if r not in record.keys():
        #           record[r] = f[1]+f[0]-1
           return(f[1]+f[0]-1)
    #for r in recordable:
    #    if r not in record.keys():
    #        record[r] = f[0]
    return f[0]

def seq_primes(k:int):
    if k in [1, 2]:
        return(k)
    d = k
    divisor = prime_div(d+1)
    while d+1 not in primes:
        d = (d+1-divisor)/divisor
        divisor = prime_div(d+1)
    return int(d)

def find_cube_seq_sum(limit:int=2*10**6):
    total = 0
    for i in range(1,limit+1):
        total += seq(i**3)
        if i % 1000==0:
            print(i, total)
    return total
start_time = time.time()
print(f"{find_cube_seq_sum()}, took {time.time()-start_time}")

#for i in range(1,100):
#    if seq(i) != seq_primes(i):
#        print(i, seq(i), seq_primes(i))
