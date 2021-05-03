def square_digit_chains(limit=100000000):
    count = 0
    nope=[1]
    for n in range(1,limit):
        #print(n)
        chain = []
        new = n
        while new != 89 and (new > n or chain == []):
            chain.append(new)
            new = sum(map(lambda x: int(x)**2, str(new)))
        if n % 1000000 == 0:
            print(f"{count} out of {n}, {count/n*100}%")
        if new not in nope:
            count += 1
        else:
            nope.append(new)
            for c in chain:
                if c not in nope and c < 1000:
                    nope.append(c)
    return(count)

print(square_digit_chains())
