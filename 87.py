import math

with open('primes.txt', 'r') as filehandle:
    primes = [int(current_prime.rstrip()) for current_prime in filehandle.readlines()]

def prime_power_triples(limit=50000000):
    worked = []
    temp_i = [i**2 for i in filter(lambda x: x<=limit**(1/2), primes)]
    temp_j = [j**3 for j in filter(lambda x: x<=limit**(1/3), primes)]
    temp_k = [k**4 for k in filter(lambda x: x<=limit**(1/4), primes)]
    for i in temp_i:
        for j in temp_j:
            for k in temp_k:
                if i+j+k < limit:
                    worked.append(i+j+k)
    #print(worked)
    #print(len(worked))
    worked = list(dict.fromkeys(worked))
    #print(len(worked))
    return len(worked)
print(prime_power_triples())
