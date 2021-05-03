import math
def max_right_triangles(limit=1500000):
    counts = {}
    squares = [x**2 for x in range(limit)]
    skip = []
    for i in range(1,limit):
        print(i)
        for j in range(int(math.sqrt(i+(i+1))),min(i,limit-i)):
            if (i, j) not in skip:
                c_squared = squares[i]+squares[j]
                if c_squared in squares:
                    c = squares.index(c_squared)
                    if i+j+c <= limit:
                        for n in range(1,int(limit/(i+j+c))+1):
                            if (i+j+c)*n not in counts.keys():
                                if n == 1:
                                    print((i,j,c))
                                counts[(i+j+c)*n] = 1
                            else:
                                counts[(i+j+c)*n] += 1
                                skip.append((i*n, j*n))
                        #if i+j+c==840:
                        #    print((i,j,c))
    return(counts)
counts = max_right_triangles()
