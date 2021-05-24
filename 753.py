import itertools
import functools
import sympy
import math

# a few helper functions, not sure how helpful they'll really be

#need this for the modulo quadratic formula
def frac_mod(n:int, d:int, p:int):
    #print(n,d,p)

    #default to regular division if you can
    n %= p
    d %= p
    if d==0:
        raise Exception("Undefined")
    check = n/d
    if int(check) == check:
        return int(check)
    if d==0 or p%d == 0:
        raise Exception("Undefined")
    # n/d = x mod p means dx = n (mod p) so if we multiply both sides by d
    # we should get dx = p*(something)+n take that mod d instead
    # 0 = p*multiplier + n (mod d) or p*multiplier = -n (mod d)
    # so if we know p mod d, that multiplier is (-n%d)/(p%d) (mod d)
    # this will always be smaller numbers, and often just be regular division
    multiplier = frac_mod(-n%d, p%d, d)
    return int((p*multiplier+n)/d)

def power_mod(base:int, exp:int, m:int):
    if exp == 0:
        return 1
    # to make this faster, we'll use a binary method
    # first, write the exponent in binary (lowest power on left)
    b = []
    while exp > 0:
        b.append(exp%2)
        exp = int(exp/2)
    powers = [base]
    for i in b[1:]:
        temp = powers[-1]**2 #find all the binary powers
        temp %= m
        powers.append(temp)
    result = [b[i]*powers[i] for i in range(len(b)) if b[i] != 0] #drop the ones with zeroes
    result = functools.reduce(lambda x, y: x*y%m, result)
    return int(result)

# using this on the difference of cubes formula
# a^3 - b^3 = (a-b)(a^2-2ab+b^2) (just the quadratic, a-b can't be 0 mod p)
# or (a+n)^3 - a^3 = 3a^2*n+3a*n^2+n^3
# could help figure out how they repeat and where
def quad_mod(a:int, b:int, c:int, mod:int): #assumes mod is a prime
    if not sympy.isprime(mod):
        raise Exception("modulus must be prime")
    # (a*x^2 + b*x + c) % mod == 0
    a %= mod
    b %= mod
    c %= mod
    #get a couple edge cases out of the way:
    if a == 0 and b != 0: #not a quadratic, bx+c = 0, so return -c/b
        try:
            result = frac_mod(-c,b,mod)
        except:
            return []
    elif a==0 and b==0:
        if c==0:
            return True
        else:
            return [] #to match our normal output

    # so I can find square roots later as needed
    #squared = [x*x%mod for x in range(mod)]
    
    #now for the actual stuff:
    # start with eliminating a
    if a != 1:
        mult = frac_mod(1,a,mod)
        a = a*mult % mod
        b = b*mult % mod
        c = c*mult % mod
    # regular completing the square
    # (x+d)^2 = (x^2+2xd + d^2)
    # so b is 2d, b/2 is d
    if b%2 == 0:
        d = int(b/2)
    else:
        d = frac_mod(b,2,mod)
    # once we do that, we have x^2 + 2d + c = 0
    # add d^2 - c to both sides
    # x^2 + 2d + d^2 = (x+d)^2 = d^2 - c
    rhs = (d*d - c)%mod
    # first check if it's a regular square number
    temp = math.sqrt(rhs)
    if int(temp) == temp:
        rhss = [int(temp), mod-int(temp)]
    else:
        # modulo square roots are a little involved
        # first check if there is one with Euler's criterion
        # +1 means yes, -1 % mod == mod-1 means no
        criterion = power_mod(rhs,(mod-1)/2,mod)
        if criterion == mod-1:
            return []
        else:
            # now actually find it
            # if mod%4 == 3 there's a shortcut
            if mod%4 == 3:
                temp = power_mod(rhs,(mod+1)/4,mod)
                if power_mod(temp, 2, mod) == rhs:
                    rhss = [temp, mod-temp]
                else:
                    return []
            else:
                #otherwise use https://en.wikipedia.org/wiki/Tonelli%E2%80%93Shanks_algorithm#The_algorithm
                Q = mod-1
                S = 0
                while Q%2 == 0:
                    Q /= 2
                    S += 1

                #find z, a number without a square root in our modulo
                z=1 #can't be 0 or 1
                while criterion == 1:
                    z += 1
                    criterion = power_mod(z,(mod-1)/2,mod)
                #prepare for looping
                M = S
                c = power_mod(z,Q,mod)
                t = power_mod(rhs,Q,mod)
                R = power_mod(rhs,(Q+1)/2,mod)
                while t not in [0, 1]:
                    temp = t
                    i=0
                    while temp != 1:
                        i += 1
                        temp = temp*temp % mod
                    b = power_mod(c,2**(M-i-1),mod)
                    M = i
                    c = b**2 % mod
                    t = (t * b**2) % mod
                    R = (R * b) % mod
                if t==0:
                    rhss=[0]
                elif t==1:
                    rhss=[int(R), mod-int(R)]
    # we have x+d = sqrt(rhs), so x = sqrt(rhs)-d (%mod)
    results = [(r-d)%mod for r in rhss]
    results.sort()
    return results

# Notes as I explore:
# F(p) is (p-1)*(p-2) when p%3 != 1 (usually p%3 is 2, but it's 0 when p==3)

#if p%3 == 1, you get (p-1)*something, starts out as multiples of 9 but that doesn't last too long

def F_naive(p:int,verbose:bool=False): #assuming p is prime
    a = [x**3%p for x in range(1,p)]
    b = [(x[0]+x[1])%p for x in itertools.product(a,a)]
    c = [x for x in list(set(b)) if x in a]
    d = [b.count(x) for x in c] #they always seem to have the same count
    if verbose:
        print(a)
        print(b)
        print(c)
        print(d)
    return sum(d)

def F(p:int,verbose:bool=False): #assuming p is prime
    if not sympy.isprime(p):
        raise Exception("p is not prime")
    if p%3 != 1: #includes the special cases of p=2 and p=3
        return (p-1)*(p-2)
    else:
        """
        skip = []
        # we'll just look in the first half, second half is the same but reversed and negative (mod p)
        a = []
        limit = int((p-1)/2)+1
        for x in range(1,limit):
            if x not in skip:
                temp = power_mod(x,3,p)
                a.append(temp)
                skip_offset = quad_mod(1,3*x,3*x**2,p)
                #skip += [x+s for s in skip_offset if x+s < limit]
                skip.append(x+skip_offset[0])
                check = x+skip_offset[1]
                if check < limit:
                    skip.append(check)
                    a.append(p-temp)
            else:
                skip.pop(skip.index(x))
        """
        # if p%3 == 1, we can fairly easily check whether any number has a cube root
        # using the Euler criterion, which should be faster than solving quadratics
        # c.f. http://m-hikari.com/ija/ija-2015/ija-5-8-2015/p/namliIJA5-8-2015.pdf
        exp = int((p-1)/3)
        limit = int((p-1)/2)+1
        checks = [power_mod(i, exp, p) for i in range(1,limit)]
        a = [i+1 for i in range(limit-1) if checks[i] == 1]
        
        # besides p = 7 and 13, these just eat up a ton of memory to spit out everything in a
        #b = [(x[0]+x[1])%p for x in itertools.product(a,a)]
        #c = [x for x in list(set(b)) if x in a]

        # the one thing I actually need to know is how many times each solution appears in b
        # but I can just check that once
        i = a[0]
        count = 0
        for j in a:
            if j-i in a: # we're really checking whether (i-j)%p is in a, but since we left out the negatives, we actually want (j-i)%p, but we know j > i, so it's just j-i
                count += 1
        count *= 2
        if limit-1 in a:
            count += 1
        if verbose:
            print(a)

        if p in [7,13]:
            return 0
        else:
            d = count*9 # 3 copies of each underlying number, two numbers added to get c[0]
            if verbose:
                print("d", d)
            return d*len(a)*2
"""
total = 0
for i in sympy.primerange(0,6*10**6):
    temp = F(i)
    total += temp
    print(i, temp)
"""
p=5999947
exp = int((p-1)/3)
limit = int((p-1)/2)+1
#checks = [power_mod(i, exp, p) for i in range(1,limit)]
#a = [i+1 for i in range(limit-1) if checks[i] == 1]
hold = 0
count = 0
for i in range(limit-1):
    current = power_mod(i,exp,p)
    if i%100000==0:
        print(i)
    if hold != 0 and current-hold == 1:
        print(i)
        count += 1
    hold = current
