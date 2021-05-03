import math

def next_half(lower=10**12):
    n=lower
    while True:
        candidate = math.ceil(math.sqrt(n*(n-1)/2))
        if candidate*(candidate-1)*2 == n*(n-1):
            print(candidate, n, candidate/n)
            n += 1
            #return candidate
        else:
            if n % 100000==0:
                print(candidate, n, abs(.5-candidate*(candidate-1)/n/(n-1))/.5, candidate/n)
            n += 1
            #print(n)
next_half(1)
