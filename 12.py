import math

def div(n):
    i = 1
    div = []
    while i <= math.sqrt(n):
        if n % i == 0:
            div.append(i)
            div.append(int(n/i))
        i += 1
    div.sort()
    return(len(div))

def highly_divisible_triangle(d=500):
    n=1
    t=1
    #m=1
    while True:
        n += 1
        t += n
        divs=div(t)
        #if divs > m:
        #    print(t, divs)
        #    m = divs
        if divs > d:
            return(t)

print(highly_divisible_triangle())
