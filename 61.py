def generate_figurate(num_shapes:int=6, digits:int=4):
    results  = []
    for s in range(3, 3+num_shapes):
        temp = []
        i=1
        j=1
        while i < 10**digits:
            i += j*(s-2)+1
            j += 1
            if 10**(digits-1)<i<10**digits:
                temp.append(i)
        results.append(temp)
    return results

storage = generate_figurate()
options = [{} for i in range(len(storage))]

for i in range(len(storage)):
    for n in storage[i]:
        for j in range(len(storage)):
            if j != i:
                for k in storage[j]:
                    if n%100 == int(k/100):
                        if n in options[i].keys():
                            options[i][n].append((k, j))
                        else:
                            options[i][n] = [(k, j)]

paths = []
for a in options[0].keys():
    paths.append([[.5]+[0]*(len(storage)-1), a]) #.5 indicates we're halfway done dealing with this one
found = False
while not found:
    temp = []
    for p in paths:
        if sum(p[0]) == 5.5:
            if p[-1]%100 == int(p[1]/100):
                print(p[1:])
                found=True
                break
        last = p[0].index(.5) #because we still need it to tell which one's next
        if p[-1] in options[last].keys():
            for o in options[last][p[-1]]:
                if p[0][o[1]] == 0:
                    p[0][last] = 1 #okay, now we're done with it
                    temp.append([p[0][:o[1]]+[.5]+p[0][o[1]+1:]] + p[1:]+[o[0]])
    if found:
        break
    paths = temp
