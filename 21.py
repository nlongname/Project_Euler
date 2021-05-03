def d(n):
    i = 2
    div = [1]
    while i <= (n/2):
        if n % i == 0:
            div.append(i)
        i += 1
    return(sum(div))

def amic_sum(limit):
    candidates = {}
    friends = []
    for n in range(limit):
        check = d(n)
        if check > n:
            candidates[n] = check
        else:
            if check in candidates.keys() and candidates[check] == n:
                friends.append(check)
                friends.append(n)
    #print(len(candidates.keys()))
    #print(sum(friends))
    return(sum(friends))

print(amic_sum(10000))
