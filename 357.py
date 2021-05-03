import math
primes = []
with open('primes.txt', 'r') as filehandle:
    primes = [int(current_prime.rstrip()) for current_prime in filehandle.readlines()]
primes = list(dict.fromkeys(primes))

def prime_divisor_pairs(n:int):
    j = int(math.sqrt(n))
    while j > 0:
        if n%j == 0 and not prime_check(j+n/j, primes):
            return False
        j -= 1
    return True

def prime_check(n:int, primes):
    if n in primes:
        return True
    elif n < primes[-1]:
        return False
    else:
        i=0
        p=primes[i]
        limit = math.sqrt(n)
        while p < limit:
            if n % p == 0:
                return False
            i += 1
            while len(primes)<i:
                primes = more_primes(primes)
            p = primes[i]
        return True                

x = 0
i = 0
total = 0
limit = 100000
while x < limit:
    while primes[i] <= primes[-1] and primes[i]-1 <= limit:
        x = primes[i]-1
        if prime_divisor_pairs(x):
            print(x)
            total += x
        i += 1
