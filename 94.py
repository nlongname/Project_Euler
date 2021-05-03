import math

def heron(a,b,c):
    hp = (a+b+c)/2
    return math.sqrt(hp*(hp-a)*(hp-b)*(hp-c))

def almost_equi(limit=1000000000):
    total = 0
    for n in range(2,int((limit-1)/3)+1):
        lower = heron(n,n,n-1)
        upper = heron(n,n,n+1)
        if int(lower) == lower:
            total += 3*n-1
            #print(n, n, n-1, lower)
        if int(upper) == upper:
            total += 3*n+1
            if n > 100000000:
                print(n, n, n+1, upper)
        if n % 1000000==0:
            print(n, total)
    return(total)
print(almost_equi())
