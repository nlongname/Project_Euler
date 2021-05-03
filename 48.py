def self_powers(limit):
    total = 0 #just last ten digits of total
    for i in range(1,limit+1):
        sp = 1
        for j in range(i):
            sp = (sp * (i % (10**10))) % (10**10)
        total = (total + sp % (10**10)) % (10**10)
    print(total)
    return total
self_powers(1000)
