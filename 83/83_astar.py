import csv
with open('p083_matrix.txt', 'r') as filehandle:
    numreader = csv.reader(filehandle, delimiter=',')
    nums = [row for row in numreader]
m = [list(map(int, nums[n])) for n in range(len(nums))]

#print(nums[0])

from numpy import *
#a = array([[131,673,234,103,18],[201,96,342,965,150],[630,803,746,422,111],[537,699,497,121,956],[805,732,524,37,331]])
#m = reshape(a, (5,5))
print(m)

storage = {}
storage[(0, 0)] = [None, m[0][0], m[0][0]+79*2] #[last node, weighted path, weightedpath + taxicab distance]
dj = [(0, 0)]
i = 0
size = len(m) #assumed square matrix
weight = min([min(r) for r in m]) #literally no help at all
while dj[i] != (size-1, size-1):
    #print(dj[i], storage[dj[i]], dj)
    last = dj[i]
    path_weight = storage[dj[i]][1]
    candidates = [(last[0]-1, last[1]), (last[0]+1, last[1]), (last[0], last[1]-1), (last[0], last[1]+1)]
    candidates = list(filter(lambda x: min(x) >= 0 and max(x) < size, candidates))
    for c in candidates:
        new_weight = path_weight + m[c[1]][c[0]]
        tc_distance = 2*(size-1)-c[1]-c[0] #straightforward taxicab distance
        tc_distance *= weight #weight by the minimum cost
        if c not in dj:
            dj.append(c)
            storage[c] = [last, new_weight, new_weight+tc_distance]
        elif dj.index(c) > i:
            if (new_weight+tc_distance) < storage[c][2]:
                storage[c] = [last, new_weight, new_weight+tc_distance]
    storage[last][2] = -1 #-1 means it's done
    dj.sort(key=lambda x: storage[x][2])
    i += 1
print(storage[dj[i]][1])
x = storage[dj[i]][0]
path = [dj[i]]
while x != None:
    path.append(x)
    x = storage[x][0]
path.reverse()
