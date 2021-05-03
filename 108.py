def find_n(pair:tuple):
    x = pair[0]
    y = pair[1]
    if (x*y) % (x+y) == 0:
        n = int((x*y)/(x+y))
        if n == 30:
            print(x, y, n)
        return n
    else:
        return False

#going diagonally through pairs of numbers, only doing the ones where y >= x to avoid dupes
test = (1, 1)
down = True
counts = {}
limit = 100
j = 0
while len(counts)==0 or max(counts.values()) < limit:
    j += 1
    for i in range(1,j+1):
        works = find_n((i, j))
        if works:
            if works in counts.keys():
                counts[works] += 1
            else:
                counts[works] = 1

for c in counts:
    if counts[c] == limit:
        print(c, counts[c])
