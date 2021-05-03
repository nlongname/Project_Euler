import math

def next_num(x, frac):
    if frac == (0, 0):
        return((x,1))
    (n, d) = frac
    temp = (d, d*x+n)
    return(temp)

def e(term):
    iterations = term-1
    if iterations % 3 != 0:
        print("No")
    else:
        k = int(iterations/3*2)
        frac = (0, 0)
        while k >= 2:
            frac = next_num(1, frac)
            frac = next_num(k, frac)
            frac = next_num(1, frac)
            k -= 2
        frac = (frac[1]*2+frac[0], frac[1])
        print(frac)
        print(sum(map(int, str(frac[0]))))
