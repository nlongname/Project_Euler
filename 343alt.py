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

record = {}

def seq(k:int):
    if k in record.keys():
        return record[k]
    f = (1, k)
    recordable=[k]
    while f[1] != 1:
        f = simp((f[0]+1, f[1]-1))
        if f[0] == 1:
            recordable.append(f[1])
    for r in recordable:
        if r not in record.keys():
            record[r] = f[0]
    return f[0]

def find_cube_seq_sum(limit:int=2*10**6):
    total = 0
    for i in range(1,limit+1):
        total += seq(i**3)
        if i % 100==0:
            print(i, len(record))
    return total
#print(find_cube_seq_sum())

for i in range(1,1000):
    if seq(i) == i:
        print(i)
