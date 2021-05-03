def distinct_powers(limit=100):
    l = []
    count = 0
    for a in range(2,limit+1):
        for b in range(2,limit+1):
            t = a**b
            if t not in l:
                l.append(t)
                count += 1
        #print(str(count)+" distinct powers so far")        
    print(str(count)+" distinct powers a^b for a, b in [2, "+str(limit)+"]")
    return(count)
distinct_powers()
