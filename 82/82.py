import csv
with open('p082_matrix.txt', 'r') as filehandle:
    numreader = csv.reader(filehandle, delimiter=',')
    nums = [row for row in numreader]
m = [list(map(int, nums[n])) for n in range(len(nums))]

#print(nums[0])

from numpy import *
#a = array([[131,673,234,103,18],[201,96,342,965,150],[630,803,746,422,111],[537,699,497,121,956],[805,732,524,37,331]])
#m = reshape(a, (5,5))
#print(m)
min_path = []
for r in range(len(m)):
    min_path.append([m[r][0]])
#print(min_path)
for c in range(len(m[0])):
    if c != 0:
        for r in range(len(m)):
            options = [0]*len(m)
            for prev_r in range(len(m)):
                for a in range(min(r, prev_r), max(r, prev_r)+1):
                    if a == prev_r:
                        options[prev_r] += min_path[prev_r][c-1]
                    else:
                        options[prev_r] += m[a][c-1]
            min_path[r].append(min(options) + m[r][c])
            #print(min_path[r][c])
possible_answers = [min_path[x][-1] for x in range(len(m))]
print(min(possible_answers))
