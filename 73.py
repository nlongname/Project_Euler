import math
record = {}

def div(n):
    i = 2
    div_list = []
    while i <= (n/2):
        if n % i == 0:
            div_list.append(i)
        i += 1
    div_list.append(n)
    record[n] = div_list
    return(div_list)

def simplify(frac):
    (n, d) = frac
    if n==1 or d==1:
        return(n,d)
    if n not in record.keys():
        div(n)
    if d not in record.keys():
        div(d)
    gcf = 1
    i = 0
    n_factors = record[n]
    n_factors.sort()
    n_factors.reverse()
    d_factors = record[d]
    d_factors.sort()
    d_factors.reverse()
    while gcf == 1 and i < len(n_factors):
        if n_factors[i] in d_factors:
            gcf = n_factors[i]
        else:
            i += 1
    return((int(n/gcf),int(d/gcf)))

def frac_between(limit=12000, lower=(1, 3), upper=(1, 2)): 
    lower = simplify(lower)
    upper = simplify(upper)
    lower_limit = lower[0]/lower[1]
    upper_limit = upper[0]/upper[1]
    curated_list = []
    d_list = range(1,limit+1)
    count = 0.0
    for d in d_list:
        for n in range(math.ceil(d*lower[0]/lower[1]),min(math.ceil(d*upper[0]/upper[1]),d)):
            #if lower_limit < n/d < upper_limit:
                #temp = simplify((n, d))
                #if temp not in curated_list:
                #    curated_list.append(temp)
            if (n, d) not in [upper, lower]:
                count += 1
            if simplify((n, d)) == (n, d):
                count -= (int(limit/d)-1)
                #print((n, d))
                #return((n,d))
    #curated_list.sort(key=lambda x: x[0]/x[1])
    #print(curated_list)
    return(int(count))
print(frac_between(8,(1,5),(1,2)))
n=0
while n < 12000:
    n += 1000
    print(n, frac_between(n))
