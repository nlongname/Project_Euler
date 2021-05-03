def interp(points, x):
    n = len(points)
    num = [1]*n
    den=[1]*n
    ans = 0
    for i in range(n):
        for j in range(n):
            if i != j:
                num[i] *= (x-j)
                den[i] *= (i-j)
    for i in range(n):
        ans += num[i]*points[i]/den[i]
    return(ans)

def u(n):
    return(1-n+n**2-n**3+n**4-n**5+n**6-n**7+n**8-n**9+n**10)

u_terms = [u(n) for n in range(1,15)]

def FIT(o:int, u_terms:list):
    i=1
    t = interp(u_terms[:o],i)
    while i < len(u_terms) and t == u_terms[i]:
        i += 1
        t = interp(u_terms[:o], i)
    if i < len(u_terms):
        return(t)
    else:
        return 0
total = 0
for i in range(1,15):
    f = FIT(i,u_terms)
    #print(f)
    total += f
print(int(total))
