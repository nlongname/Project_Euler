def lychrel(limit, iterations=50):
    candidates=[]
    skip=[]
    for n in range(1,limit):
        #if n == 887:
        #    print(887)
        if n not in skip and n not in candidates:
            i=0
            reverse=int(str(n)[::-1])
            new = n+reverse
            thread = [n, new]
            while i < iterations and reverse != new:
                reverse = int(str(new)[::-1])
                if reverse != new:
                    new += reverse
                    i += 1
            if reverse != new:
                #print(n)
                for t in thread[:-1]:
                    if t < limit and t not in candidates:
                        candidates.append(t)
                candidates.sort()
            #else:
            #    for t in thread[:-1]:
            #        skip.append(t)
    print(candidates)
    print(len(candidates))
    return(len(candidates))

lychrel(10000)
