# https://projecteuler.net/problem=91
# Consider a triangle between the origin and two points, (x1, y1) and (x2, y2)
# Where x1, y1, x2, and y2 are all integers between 0 and 50 inclusive
# How many of those possible triangles have a right angle?

import itertools

def dp(v:tuple, w:tuple):#dot product, assuming 2d for simplicity
    return(v[0]*w[0]+v[1]*w[1])

def check_rightness(a:tuple, b:tuple):
    c=(0,0)#assumed, so two of the vectors are a and b
    u=(a[0]-b[0], a[1]-b[1]) #third vector is between the points a and b
    if dp(u, a) == 0: #dot product is 0 if and only if the two vectors are perpendicular
        return True
    elif dp(u, b) == 0:
        return True
    elif dp(a,b) == 0:
        return True
    else:
        return False

def find_rights(side_length=50):
    count=0
    points = [(x, y) for x in range(side_length+1) for y in range(side_length+1)]
    for i in points:
        if i != (0, 0):
            for j in points:
                if j != (0, 0):
                    if i != j:
                        if check_rightness(i,j):
                            count += 1
    return(int(count/2))#we're double-counting everything

print(find_rights())
