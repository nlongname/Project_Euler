from fractions import *
import csv

with open('p102_triangles.txt', newline='') as f:
    nums = [line.rstrip('\n') for line in f]

def origin(l:list): #assumed to be three 2-d coordinates
    a = l[0]
    b = l[1]
    c = l[2]
    intercepts = []
    if a[0] != b[0]:
        m = Fraction((b[1]-a[1]), (b[0]-a[0]))
        intercept = a[1] - m*a[0]
        if min(a[1], b[1]) <= intercept <= max(a[1], b[1]):
            intercepts.append(intercept)
    if c[0] != a[0]:
        m = Fraction((c[1]-a[1]), (c[0]-a[0]))
        intercept = a[1] - m*a[0]
        if min(a[1], c[1]) <= intercept <= max(a[1], c[1]):
            intercepts.append(intercept)
    if len(intercepts)==0:
        return False #no point checking the third if the first two don't work
    if b[0] != c[0]:
        m = Fraction((c[1]-b[1]), (c[0]-b[0]))
        intercept = b[1] - m*b[0]
        if min(b[1], c[1]) <= intercept <= max(b[1], c[1]):
            intercepts.append(intercept)
    #print(intercepts)
    if len(intercepts) == 2:
        if abs(intercepts[0] - intercepts[1]) > max(abs(intercepts[0]), abs(intercepts[1])):
            return True
    return False

answer = 0
for n in nums:
    even = False
    points = []
    while ',' in n:
        comma = n.index(',')
        if even == True:
            points.append((temp, int(n[:comma])))
            even = False
        else:
            temp = int(n[:comma])
            even = True
        n = n[comma+1:]
    points.append((temp, int(n)))
    if origin(points):
        answer += 1
print(answer)
