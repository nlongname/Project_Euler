import math, time
start_time = time.time()

primes = []
with open('primes.txt', 'r') as filehandle:
    primes = [int(current_prime.rstrip()) for current_prime in filehandle.readlines()]

def distinct_prime_factors(n):
    i = 0
    count = 0
    while primes[i] <= (n/2):
        if n % primes[i] == 0:
            count += 1
        i += 1
    return(count)

def find_string(l=4):
    n=1
    string = 0
    while string < l:
        string = 0
        while n not in primes and distinct_prime_factors(n) == l:
            n += 1
            string += 1
            #if string > 2:
            #    print(n-1, n)
        n += 1
        #if n % 1000 == 0:
        #    print(n, time.time()-start_time)
    print(n-l-1)
    return(n-l-1)
find_string(4)
#print((time.time()-start_time), "seconds")
