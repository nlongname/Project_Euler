import math

divisors = {}

def div(n):
    i = 2
    div_list = []
    while i <= math.sqrt(n):
        if n % i == 0:
            div_list.append(i)
            div_list.append(n/i)
        i += 1
    div_list.append(n)
    div_list.sort()
    divisors[n] = div_list
    return(div_list)

def simplify(n, d):
    if n==1 or d==1:
        return(n,d)
    if n not in divisors.keys():
        div(n)
    if d not in divisors.keys():
        div(d)
    gcf = 1
    i = 0
    n_factors = divisors[n]
    n_factors.sort()
    n_factors.reverse()
    d_factors = divisors[d]
    d_factors.sort()
    d_factors.reverse()
    while gcf == 1 and i < len(n_factors):
        if n_factors[i] in d_factors:
            gcf = n_factors[i]
        else:
            i += 1
    return((int(n/gcf),int(d/gcf)))

results = {}
def sequence(num, den):
    hold = []
    while (num, den) not in results.keys() and den != 1:
        if num==1:
            hold.append((num, den))
        (num, den) = simplify(num+1, den-1)
    if (num, den) in results.keys():
        #print((num, den))
        answer = results[(num, den)]
    else:
        answer = num
    for h in hold:
        results[h] = answer
    return(answer)
        
def f(k):
    return(sequence(1,k))

def main(p):
    total = 0
    for k in range(1,2*10**p+1):
        total += f(k**3)
        if k % 100 == 0:
            print((k, total))
    print(total)
