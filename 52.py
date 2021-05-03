def digits(n:int):
    ans={}
    n = str(n)
    for d in n:
        if d in ans.keys():
            ans[d] += 1
        else:
            ans[d] = 1
    return ans

def perm_mult(multiples:int=6):
    i=1
    x=0
    while x != multiples:
        check = digits(i)
        for x in range(2,multiples+1):
            if digits(x*i) != check:
                i += 1
                #if i == 125874:
                #    print(i)
                break
    return i
print(perm_mult(6))
