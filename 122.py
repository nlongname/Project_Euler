def many_chains(goal, chains=[[1]]): #works great up to about 15 or so, but it gets exponentially worse as it goes
    unfinished_chains = [c for c in chains if c[-1] != goal]
    finished_chains = [c for c in chains if c not in unfinished_chains]
    if len(unfinished_chains) == 0:
        return min([len(c) for c in chains])-1 # the 1 doesn't count, because it's not actually a multiplication
    new_chains = []
    for c in unfinished_chains:
        if goal not in c:
            y=c[-1]
            for x in c:
                if x+y not in c and x+y <= goal:
                    new_chains.append(c + [x+y])
    return many_chains(goal, new_chains + finished_chains)

def chain_list(goal:int=200):
    cl = [[[]],[[1]]]
    while goal >= len(cl):
        next_num = len(cl)
        min_paths = []
        min_length = 0
        for i in range(int(next_num/2),next_num):
            for l in cl[i]:
                if (next_num - i) in l:
                    if min_length == 0 or min_length > (len(l)+1):
                        min_paths = [l + [next_num]]
                        min_length = len(min_paths[0])
                    elif min_length == len(l)+1:
                        min_paths.append(l+[next_num])
        cl.append(min_paths)
    cl = [x[0] for x in cl[1:]]
    cl = [len(x)-1 for x in cl] #subtract one because they all include 1, which takes 0 multiplications
    return sum(cl)

print(chain_list())
