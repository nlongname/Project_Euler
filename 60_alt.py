# https://projecteuler.net/problem=60
# We want a set of 5 primes such that each pair, when concatenated, is prime
# e.g. (3, 7) -> 37 and 73 are both prime
# return the minimum sum of 5 such primes

from sympy import primerange, isprime

#def prime_pair_set(prime_max:int=5000) -> list:
prime_max = 10000
n=5 #had to hard-code this in the end
primes = set(primerange(1,prime_max))
pairs = {}
for p in primes:
    if p not in [2,5]:
        for q in primes:
            if q not in [2,5] and q > p and (p not in pairs or q not in pairs[p]):
                if isprime(int(str(p)+str(q))) and isprime(int(str(q)+str(p))):
                    pairs[p] = [q] if p not in pairs else pairs[p]+[q]
                    pairs[q] = [p] if q not in pairs else pairs[q]+[p]

pair_list = {(x, y):[u for u in pairs[x] if u in pairs[y]] for x in pairs for y in pairs[x] if y > x}
pair_list = {p:pair_list[p] for p in pair_list if pair_list[p] != []}
trip_list = {(a,b,c):[x for x in pair_list[a,b] if x in pair_list[a,c] and x in pair_list[b,c]] for (a,b) in pair_list for c in primes if (b,c) in pair_list and (a,c) in pair_list and c > b}
trip_list = {t:trip_list[t] for t in trip_list if trip_list[t] != []}
quad_list = {(a,b,c,d):[x for x in trip_list[a,b,c] if x in trip_list[a,b,d] and x in trip_list[a,c,d] and x in trip_list[b,c,d]] for (a,b,c) in trip_list for d in primes if (a,b,d) in trip_list and (a,c,d) in trip_list and (b,c,d) in trip_list and d>c}
quad_list = {q:quad_list[q] for q in quad_list if quad_list[q] != []}
minimum = min(quad_list, key=lambda x: x[0]+x[1]+x[2]+x[3]+quad_list[x][0])
minimum = list(minimum + (quad_list[minimum][0],))
minimum.sort()
print(minimum, sum(minimum))
