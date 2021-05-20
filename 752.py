# https://projecteuler.net/problem=752
# for each x, we're looking for g(x), the lowest power n where (1+sqrt(7))^n
# has the coefficients a + b*sqrt(7) with a%n == 1 and b%n == 0
# If no such n exists, g(x) = 0
# Find the sum of g(x) for 2 <= x <= 10**6

# This is an alteration of the Pascal's triangle method of finding binomials
# If we have coefficients a_n and b_n for one iteration
# For the next we get a_n + 7b_n and a_n + b_n
# First few: (1, 1), (8, 2), (22, 10)

# However, since all we care about is their value mod x
# We'll be calculating them mod x each time
# Obviously we'll be recalculating some things, but at least we'll know when to stop
# If it reaches (1, 0), we return how many steps it took
# If it cycles, we return 0

# observations going through:
# g(x)=0 for 2 and 3, as well as all multiples of 2 and 3
# once you get (n, 0), the next time that happens you get
# ((n**2)%x, 0), then ((n**3)%x, 0) and so on until you get to (1, 0)
# (or for multiples of 2 or 3 you cycle)

primes = []
with open('primes.txt', 'r') as filehandle:
    primes = [int(current_prime.rstrip()) for current_prime in filehandle.readlines()]
primes = list(dict.fromkeys(primes)) #remove duplicates, just in case
primes.sort() #sort them, since dict keys aren't guaranteed to be in order

def g_naive(x:int):
    link = None
    chain = [(1, 1)]
    while link not in chain[:-1] and link != (1, 0):
        link = ((chain[-1][0]+7*chain[-1][1])%x, (chain[-1][0]+chain[-1][1])%x)
        chain.append(link)
    print(x, chain)
    if link == (1, 0):
        return len(chain)
    else:
        return 0

def g_chain(x:int):
    link = [None, None]
    chain = [(1, 1)] #keeping chain is theoretically necessary to detect 0's, but I'm avoiding all of them already
    while link not in chain[:-1] and link[1] != 0:
        link = ((chain[-1][0]+7*chain[-1][1])%x, (chain[-1][0]+chain[-1][1])%x)
        chain.append(link)
    if link in chain[:-1] or link[0] == 0:
        print(len(chain))
        return 0
    elif link[0] == 1: # meaning our link is (1, 0), so we're done
        return len(chain)
    else: # we have (n, 0), n != 1
        base = link[0]
        length = len(chain)
        #print(x, base, length)
        exp = 1
        temp = base
        while temp != 1:
            temp *= base
            temp %= x
            exp += 1
        return exp*length

def g(x:int):
    if x == 1 or x%2 == 0 or x%3 == 0:
        return 0
    else:
        link = (1,1)
        length = 1
        while link[1] != 0:
            link = ((link[0]+7*link[1])%x, (link[0]+link[1])%x)
            length += 1
        base = link[0]
        exp = 1
        temp = base
        while temp != 1:
            temp *= base
            temp %= x
            exp += 1
        return exp*length
    
            
def g_sum(upper:int, lower:int=2): #assumed to be inclusive, and starting at 2
    total = 0
    longest_chain = 0
    if lower % 2 == 0:
        lower += 1 #always start on odd, evens never work
    for x in range(lower, upper+1,2):
        if x % 3 != 0: #neither do multiples of 3
            total += g(x)
        if x % 10**4 == 1:
            print(x)
    return total

print(g_sum(10**6))
# 5610899769745488

#This is way too slow, but it does work
#Biggest problem seems to be how long it takes to find the first (n, 0)
#After that, I would think it's how long it takes to find the right power to get (1, 0)
