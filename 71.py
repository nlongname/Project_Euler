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

def simplify(n, d):
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

def left_of(limit=1000000, a=3, b=7):
    upper_limit = a/b
    lower_num = int(a/b*limit)
    lower_den = limit
    (lower_num, lower_den) = simplify(lower_num, lower_den)
    lower_limit = lower_num / lower_den
    curated_list = [(lower_num, lower_den), (a, b)]
    d_list = range(1,limit+1)
    d_list = d_list[::-1]
    for d in d_list:
        for n in range(math.ceil(d*lower_num/lower_den),min(math.ceil(d*a/b),d)):
            if lower_limit < n/d < a/b:
                (temp_num, temp_den) = simplify(n, d)
                curated_list.append((temp_num, temp_den))
                print(((n, d),(temp_num,temp_den)))
                #return((n,d))
    curated_list.sort(key=lambda x: x[0]/x[1])
    print(curated_list)
    return(curated_list[-2])

left_of(999)
