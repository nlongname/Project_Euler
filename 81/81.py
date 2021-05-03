import csv
with open('p081_matrix.txt', 'r') as filehandle:
    numreader = csv.reader(filehandle, delimiter=',')
    nums = [row for row in numreader]
m = [list(map(int, nums[n])) for n in range(len(nums))]

#print(nums[0])

#from numpy import *
#a = array([[131,673,234,103,18],[201,96,342,965,150],[630,803,746,422,111],[537,699,497,121,956],[805,732,524,37,331]])
#m = reshape(a, (5,5))
#print(m)

r = 0
for c in range(len(m[0])):
    if c != 0:
        m[0][c] += m[0][c-1]
r = 1
while r < len(m):
    for c in range(len(m[r])):
        if c == 0:
            m[r][c] += m[r-1][c]
        else:
            m[r][c] += min(m[r-1][c], m[r][c-1])
    r += 1
print(m[-1][-1])
