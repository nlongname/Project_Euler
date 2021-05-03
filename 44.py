import time
start_time = time.time()

saved = []

def pentagon_pairs(limit=1000, saved=[]):
    pentagons = [1]
    n = 1
    while n<limit:
        pentagons.append(pentagons[-1]+3*n+1)
        n += 1
    #print(pentagons)
    for p in pentagons:
        i = pentagons.index(p)
        for j in range(i):
            if pentagons[i] - pentagons[j] in pentagons:
                while pentagons[i]+pentagons[j] > pentagons[-1]:
                    pentagons = more_pentagons(pentagons)
                    print(len(pentagons), "pentagons isn't enough")
                if pentagons[i]+pentagons[j] in pentagons:
                    print((pentagons[i], pentagons[j]))
                    print(pentagons[i]-pentagons[j])
                    return((pentagons[i], pentagons[j]))

def more_pentagons(pentagons):
    n = len(pentagons)
    for i in range(100):
        pentagons.append(pentagons[-1]+3*n+1)
        n += 1
    return(pentagons)

pentagon_pairs()
print("%s seconds" % (time.time()-start_time))
