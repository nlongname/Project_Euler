import math

primes = []
with open('primes.txt', 'r') as filehandle:
    primes = [int(current_prime.rstrip()) for current_prime in filehandle.readlines()]

def check_prime(n):
    if n in primes:
        return(True)
    for p in primes:
        if p > math.sqrt(n):
            return(True)
        elif n % p == 0:
            return(False)

n=1
last = 1
diagonals = 1
p = 0
warning_count = 0
while p == 0 or p*10 >= diagonals:
    n += 2
    #n^2 - (n-2)^2 = n^2 - (n^2 -4n + 4) = 4n - 4 is the increment to the last of the next spiral
    #n-1 is the increment between each number in the spiral
    #so our options are (last + n-1), (last + 2n - 2), (last + 3n - 3), [(last + 4n-4)]
    #we ignore the last one because it's always an square number
    #combining like terms:
    candidates = [last + n-1, last + 2*n - 2, last + 3*n - 3]
    for c in candidates:
        if check_prime(c):
            p += 1
    diagonals += 4
    last += 4*n-4
    if n % 100 == 1:
        print(n, last, p/diagonals)
print(n)
