def direction(x:str, y:str):
    x = int(x)
    y = int(y)
    if x < y:
        return 1 #increasing
    if x == y:
        return 0 #same
    if x > y:
        return -1

def bouncy(n:int or str):
    n = str(n)
    dirs = [direction(n[i], n[i+1]) for i in range(len(n)-1)]
    dirs = list(filter(None, dirs))
    if abs(sum(dirs)) != len(dirs):
        return True
    else:
        return False
count = 0
i = 1
while (count / i) < .99:
    i += 1
    if bouncy(i):
        count += 1
print(i)
