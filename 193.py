primes = []
with open('primes.txt', 'r') as filehandle:
    primes = [int(current_prime.rstrip()) for current_prime in filehandle.readlines()]

product = 1
for p in primes:
    if product < 2**50:
        product *= p
    else:
        print(primes.index(p), p, product)
        break
