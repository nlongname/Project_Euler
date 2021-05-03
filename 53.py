import math

def binomial(n:int, r:int):
    return int(math.factorial(n)/math.factorial(r)/math.factorial(n-r))

def bin_over(limit:int=10**6, n_limit:int=100):
    total = 0
    for n in range(1,n_limit+1):
        check = n
        i=1 #skip i=0 because it's always 1
        while check <= limit and i <= int(n/2):
            i += 1
            check = binomial(n,i)
        if check > limit:
#            print((n, i))
            total += (n-i)-i+1 #n-i is the other one with the same value, so subtract i from that and add 1 to get the number
    return(total)

print(bin_over())
