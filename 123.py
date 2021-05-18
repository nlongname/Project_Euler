# https://projecteuler.net/problem=123
# very similar to #120, see more detailed calculations there
# for odd numbers n, the remainder is 2*n*p_n
# for even numbers, the remainder is 2

primes = []
with open('primes.txt', 'r') as filehandle:
    primes = [int(current_prime.rstrip()) for current_prime in filehandle.readlines()]
primes = list(dict.fromkeys(primes)) #remove duplicates, just in case
primes.sort() #sort them, since dict keys aren't guaranteed to be in order

n = 1
while n*primes[n-1]*2 < 10**10:
    n += 2 #skip the even ones
print(n)
