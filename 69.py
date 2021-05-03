def gcf(x:int, y:int):
    b = max(x, y)
    s = min(x, y)
    while s != 0:
        b = b-s*(int(b/s))
        temp = b
        b = s
        s = temp
    return(b)
max_test = 1
for i in range(2,10**6):
    count = 0
    for j in range(1,i):
        if gcf(i,j) == 1:
            count += 1
    test = i/count
    if test > max_test:
        max_test = test
        print((i, count, test))
