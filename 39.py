#import itertools
counts = [0]*1001

def max_right_triangles(limit=1000):
    squares = [x**2 for x in range(limit)]
    for i in range(1,limit):
        for j in range(1,min(i,limit-i)):
            c_squared = squares[i]+squares[j]
            if c_squared in squares:
                c = squares.index(c_squared)
                if i+j+c <= limit:
                    counts[i+j+c] += 1
                    #if i+j+c==840:
                    #    print((i,j,c))
    return(counts)
counts = max_right_triangles()
print(counts.index(max(counts)))
