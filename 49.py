import math, itertools

primes = []
with open('primes.txt', 'r') as filehandle:
    primes = [int(current_prime.rstrip()) for current_prime in filehandle.readlines()]

def prime_perms(l=4):
    candidates = [p for p in primes if len(str(p))==l]
    for c in candidates:
        chain = [c]
        for perm in itertools.permutations(str(c)):
            s = ''
            for d in perm:
                s += d
            s = int(s)
            if s not in chain and s in candidates:
                chain.append(s)
        if len(chain) >= 3:
            for n in chain[1:]:
                if (n-c)+n in chain:
                    print(c, n, (n-c)+n)
prime_perms()
