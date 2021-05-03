def frac(i:int, j=None):
    if type(i) == tuple:
        return(i)
    if j != None:
        return(i, j)
    else:
        return((i, 1))

def lcm(x:int, y:int):
    return(int(x*y/gcf(x,y)))

def gcf(x:int, y:int):
    b = max(x, y)
    s = min(x, y)
    while s != 0:
        b = b-s*(int(b/s))
        temp = b
        b = s
        s = temp
    return(b)

def simp(a:tuple or int, b=None):
    if b != None:
        a = (a, b)
    if type(a)==int:
        return(frac(a))
    else:
        g = gcf(a[0],a[1])
        n = int(a[0]/g)
        d = int(a[1]/g)
        return((n,d))

def plus(a:tuple, b:tuple):
    if type(a) == int:
        a = frac(a)
    if type(b) == int:
        b = frac(b)
    d = lcm(a[1], b[1])
    n = int(a[0]*d/a[1] + b[0]*d/b[1])
    return(simp(n,d))

def mult(a:tuple, b:tuple):
    return(simp(a[0]*b[0],a[1]*b[1]))

def recip(a):
    if type(a)==int:
        a = frac(a)
    return((a[1],a[0]))

def series(a:tuple, b:tuple):
    return(recip(plus(recip(a),recip(b))))

def capacitors(limit=18, capac=60):
    if type(capac) == int:
        capac = frac(capac)
    results = [[],[capac]]
    done = []
    for n in range(2,limit+1):
        print(n, len(results[-1]))
        temp = []
        for i in range(1,int(n/2)+1):
            for j in results[i]:
                for k in results[n-i]: #k >= j
                    if (j, k) not in done:
                        para = plus(j,k)
                        seri = series(j,k)
                        done.append((j,k))
                    for option in (para, seri):
                        if option not in temp:
                            temp.append(option)
        results.append(temp)
    answer = []
    for i in results:
        answer += i
    answer = list(dict.fromkeys(answer))
    answer.sort(key=lambda x: x[0]/x[1])
    return(answer)

ans = capacitors(18,1)
