import math

def brute_pascal(rows, mod=7):
    r = [1]
    total=1
    #print(r)
    row_count=1
    while row_count<rows:
        row_count += 1
        r = [1]+[(r[i]+r[i+1])%mod for i in range(len(r)-1)]+[1]
        #print(r)
        total += row_count - r.count(0)
        #print(r)
        #if row_count ==rows:
            #print(r)
            #print(row_count, total)
    return total

def calc_pascal(rows, mod=7):
    if rows <= mod:
        return(int(rows*(rows+1)/2))
    exp = int(math.log(rows,mod))
    n = int(rows/7**exp)
    rows_left = rows-n*7**exp
    num_triangles = int(n*(n+1)/2)
    total = num_triangles*((mod*(mod+1))/2)**exp
    if rows_left != 0:
        total += (n+1)*calc_pascal(rows_left, mod)
    return(int(total))

print(calc_pascal(10**9))
#print(brute_pascal(1000))
