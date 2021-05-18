# https://projecteuler.net/problem=94
# find the sum of all "almost equilateral" triangles with integer area
# limited to a perimeter below 10**9
# almost equilateral meaning two sides are equal and the third is one off
# e.g. a 5/5/6 triangle has an area of 12

import math

def heron(a,b,c):
    hp = (a+b+c)/2
    return math.sqrt(hp*(hp-a)*(hp-b)*(hp-c))

#gets tons of false positives when the numbers get too big for floats
def almost_equi_naive(limit=1000000000):
    total = 0
    for n in range(2,int((limit-1)/3)+1):
        lower = heron(n,n,n-1)
        upper = heron(n,n,n+1)
        if int(lower) == lower:
            total += 3*n-1
            #print(n, n, n-1, lower)
        if int(upper) == upper:
            total += 3*n+1
            if n > 100000000:
                print(n, n, n+1, upper)
        if n % 1000000==0:
            print(n, total)
    return(total)

# a lot of mysterious numbers here, but for a rough overview:
# we're using a different version of Heron's formula:
# A = 1/4 * sqrt((a+b+c)(-a+b+c)(a-b+c)(a+b-c))

# for a, a, a+1 we get (a+1)/4 * sqrt((3a+1)(a-1))
# and have solutions when both (3a+1) and (a-1) are square numbers
# d is the difference between the square roots of those two terms
# solve a couple quadratics and you find it only works when
# l^2 = 3d^2 - 8 for some l, so we're checking all possible l
# to see when d is an integer, in which case it works out

# for a, a, a-1 we get (a-1)/4 * sqrt((3a-1)(a+1))
# this never gives us two square numbers for (3a-1)(a+1)
# but we can have one be 2x^2 and the other 2y^2 so the square root is 2xy
# since the bigger one is 4 less than 3 times the smaller we have 3(2x^2)-4 = 2y^2
# y^2 = 3x^2 - 2, we check all possible y to see if you get x as an integer

# once we've found d or x, it's easy to find a and add the perimeter to the total


plus_flag=True
minus_flag=True
i=1
total = 0
while plus_flag or minus_flag:
    if i%3 != 0:
        if plus_flag:
            temp = (i**2+8)/3
            if int(math.sqrt(temp))**2 == temp:
                d = math.sqrt(temp)
                a = int((d + math.sqrt(3*temp-8))/2)**2+1
                area = (a+1)/4 * math.sqrt((3*a+1)*(a-1))
                if int(area) != area:
                    print(a)
                if a > (10**9-1)/3:
                    plus_flag=False
                else:
                    total += 3*a+1
                    #print(i, a, "plus", 3*a+1, total)
        if minus_flag and i > 1: #have to avoid the 1/1/0 triangle
            temp = (i**2+2)/3
            if int(math.sqrt(temp))**2 == temp:
                a = int(2*temp-1)
                area = (a-1)/4*math.sqrt((3*a-1)*(a+1))
                if int(area) != area:
                    print(a)
                if a > (10**9+1)/3:
                    minus_flag = False
                else:
                    total += 3*a-1
                    #print(i, a, "minus", 3*a-1, total)
    i += 1
print(total)
