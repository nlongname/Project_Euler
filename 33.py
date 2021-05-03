record = {}
import math

def div(n):
    i = 2
    div_list = []
    while i <= math.sqrt(n):
        if n % i == 0:
            div_list.append(i)
            div_list.append(int(n/i))
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
    

results = []
for i in range(11,100):
    #print(i)
    for j in range(11,i):
        if i % 10 != 0 and j % 10 != 0:
            i_t = int(i/10) #tens digit
            i_o = int(i - 10*i_t) #ones digit
            j_t = int(j/10)
            j_o = int(j - 10*j_t)
            if j_t == i_t:
                if simplify(j_o, i_o) == simplify(j, i):
                    print((j, i))
                    results.append((j,i))
            if j_t == i_o:
                if simplify(j_o, i_t) == simplify(j, i):
                    print((j,i))
                    results.append((j,i))
            if j_o == i_o:
                if simplify(j_t, i_t) == simplify(j, i):
                    print((j,i))
                    results.append((j,i))
            if j_o == i_t:
                if simplify(j_t, i_o) == simplify(j, i):
                    print((j,i))
                    results.append((j,i))
n=1
d=1
for r in results:
    n *= r[0]
    d *= r[1]
print(simplify(n,d)[1])
