import math
def max_right_triangles(limit=1500000):
    counts = {}
    #squares = [x**2 for x in range(limit)]
    skip = {}
    failures = []
    for i in range(1,limit):
        if i % 10 ==  0 or 440<i<450:
            print(i)
        for j in range(int(math.sqrt(i+(i+1))),min(i,limit-i)):
            if i == 448:
                print(j)
            if (i not in skip.keys() or j not in skip[i]) and i%2 != j % 2:
                i_squared = i**2
                j_squared = j**2
                c_squared = i_squared + j_squared
                c = math.sqrt(c_squared)
                if int(c) == c:
                    c = int(c)
                    if i+j+c <= limit:
                        for n in range(1,int(limit/(i+j+c))+1):
                            l = (i+j+c)*n
                            if l not in failures:
                                if l not in counts.keys():
                                    if n == 1:
                                        print((i,j,c), len(skip))
                                    counts[l] = 1
                                else:
                                    counts[l] += 1
                                    #failures.append(l)
                            if n != 1:
                                if i*n in skip.keys():
                                    skip[i*n].append(j*n)
                                else:
                                    skip[i*n] = [j*n]
                        #if i+j+c==840:
                        #    print((i,j,c))
                else:
                    for n in range(2,int(limit/(i+j+c))+1):
                        if  n != 1:
                            if i*n in skip.keys():
                                skip[i*n].append(j*n)
                            else:
                                skip[i*n] = [j*n]
        if i in skip.keys():
            #print(skip[i])
            skip.pop(i)
    return(counts.keys())

one_offs = sum(max_right_triangles())
print(one_offs)
