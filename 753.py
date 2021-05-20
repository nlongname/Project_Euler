import itertools
import sympy

# Notes as I explore:
# F(p) is (p-1)*(p-2) when p%3 != 1 (usually p%3 is 2, but it's 0 when p==3)

#if p%3 == 1, you get (p-1)/3 * (some multiple of 9)

def F(p:int): #I'm assuming p is a prime, but I don't think it actually makes a difference in this function
    a = [x**3%p for x in range(1,p)]
    #print(a)
    b = [(x[0]+x[1])%p for x in itertools.product(a,a)]
    #print(b)
    c = [x for x in list(set(b)) if x in a]
    #print(c)
    d = [b.count(x) for x in c] #they always seem to have the same count
    print(d)
    return sum(d)


for i in sympy.primerange(0,10**2):
    if i%3==1:
        temp = F(i)
        print(i,temp, temp/(i-1))


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

# using this on the difference of cubes formula
# a^3 - b^3 = (a-b)(a^2-2ab+b^2) (just the quadratic, a-b can't be 0 mod p)
# or (a+n)^3 - a^3 = 3a^2*n+3a*n^2+n^3
# could help figure out how they repeat and where
def quad_mod(a:int, b:int, c:int, mod:int):
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
    squared = [x*x%mod for x in range(mod)]
    
    #now for the actual stuff:
    # start with eliminating a
    try:
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
        # I don't think it's worth finding prime factorization, chinese remainder theorem, etc
        # so we just brute forced the square root
        # we have x+d = sqrt(rhs), so x = sqrt(rhs)-d (%mod)
        results = []
        for i in range(mod):
            if squared[i] == rhs:
                results.append((i-d)%mod)
        return results
    
    except:
        if a==1:
            #then something went wrong later in the process that I can't fix
            return []
        else:
            #it's possible for a to have a square root, but no inverse
            #if you're lucky you can sometimes complete the square
            # say sqrt(a) is o, we want o^2*x^2+2odx+d^2 = (ox+d)^2
            options = [x for x in range(mod) if squared[x]==a]
            ds = []
            for o in options:
                try:
                    ds.append(frac_mod(b,2*o, mod))
                except:
                    ds.append(None)
            # if that worked, we have o^2*x^2 + 2odx + c = 0, add d^2-c to both sides
            # to get (ox+d)^2 = d^2-c
            rhss = []
            for d in ds:
                if d != None:
                    temp = (d*d-c)%mod
                    rhss.append([i for i in range(mod) if squared[i]==temp])
                else:
                    rhss.append([])
            # ox+d = sqrt(d^2-c)
            results=[]
            for i in range(len(rhss)):
                if rhss[i] != []:
                    for r in rhss[i]:
                        try:
                            temp = frac_mod(r-ds[i], options[i], mod)
                            results.append(temp)
                        except:
                            next
            results = list(set(results))
            results.sort()
            return results

# went a little overboard on that, many edge cases weren't necessary for this
# I just thought it was cool, and tried to make it work as thoroughly as possible
# turns out solving modulo quadratics is harder than I expected
# there are a lot of weird cases where completing the square doesn't work
# even when there are fairly obvious answers by inspection
# especially with an even modulus

# Since we're only using prime modulus, I'm going to pare this down to the things I actually need
