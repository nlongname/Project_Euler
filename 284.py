import time
start_time = time.time()

def mult(x, y, base=14):#base-indep. mult. using lists
    if [] in [x, y]:
        return []
    if len(x) > len(y):
        s = y
        b = x
    else:
        s=x
        b=y
    ans = [0]*(len(s)+len(b))
    for d in range(len(s)):
        if s[d] >= base:
            raise ValueError("A digit is too big for that base")
        for e in range(len(b)):
            temp = s[d]*b[e]
            ans[d+e] += temp
    for i in range(len(ans)):
        if ans[i] >= base:
            ans[i+1] += int(ans[i]/base)
            ans[i] = ans[i]%base
    while ans != [] and ans[-1] == 0:
        ans = ans[:-1]
    return(ans)

def plus(x,y, base=14):#base-indep. add. using lists
    if x == []:
        return y
    if y == []:
        return x
    if len(x) > len(y):
        s = y
        b = x
    else:
        s = x
        b = y
    ans = b+[0]
    for i in range(len(s)):
        ans[i] += s[i]
    for i in range(len(ans)):
        if ans[i] >= base:
            ans[i+1] += int(ans[i]/base)
            ans[i] = ans[i]%base
    if ans[-1] == 0:
        ans = ans[:-1]
    return(ans)

def sum_of_digits(x, base=14):
    ans=[]
    for d in x:
        ans = plus(ans,[d])
    return(ans)

def steady_squares(max_digits=10000, base=14):
    ss=[]
    total = []
    for n in range(1,base): #setting up first digits is a little different
        temp = [n]
        if mult(temp,temp, base)[:1] == temp:
            ss.append(temp)
            total = plus(total,sum_of_digits(temp), base)
            #print(temp, total)
    for d in range(2,max_digits+1):
        new_ss = ss[::1]
        for s in ss:
            buffer = [0]*(d-len(s)-1)
            for n in range(base):
                temp = s+buffer+[n]
                if mult(temp,temp, base)[:d] == temp:
                    new_ss.remove(s)
                    new_ss.append(temp)
                    if d == max_digits:
                        print(temp)
                    if n != 0:
                        total = plus(total,sum_of_digits(temp), base)
                    if d == max_digits:
                        print(temp, total)
        if d % 100 == 0:
            print(d, total)
        ss = new_ss[::1]
def steady_squares_direct(max_digits=10000, base=14):
    ssd = []
    total = [1] #skip 1 because it leads immediately to an impossible inverse
    count = 0
    next_dig=[]
    for n in range(2,base): #setting up first digits is a little different
        temp = [n]
        squared = mult(temp,temp,base)
        if squared[:1] == temp:
            ssd.append(temp)
            total = plus(total,sum_of_digits(temp), base)
            #print(temp, total)
            if len(squared) > 1:
                next_dig.append(squared[1])
            else:
                next_dig.append(0)
    inv = {1:1, 3:5, 5:3, 9:11, 11:9, 13:13}
    a = [0]*len(ssd)
    for d in range(2,max_digits+1):
        for i in range(len(ssd)):
            a[i] = ((base-next_dig[i])*inv[(2*ssd[i][0]-1)%base])%base
            ssd[i]. append(a[i])
            next_dig[i] = mult(ssd[i],ssd[i])[d]#(((a[i]**2)%base)+int(2*a[i]*ssd[i][0]/base))%base
            if d == max_digits:
                print(ssd[i])
    return(ssd)

#steady_squares(100)
#print("next")
steady_squares_direct(10000)
#n=[1]
#total = []
#for i in range(7**10):
#    if mult(n,n)[:len(n)] == n:
#        total = plus(total,sum_of_digits(n))
#        print(n, total)
#    n = plus(n,[1])
#    #print(n)

print(time.time()-start_time, "seconds")

