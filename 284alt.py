# https://projecteuler.net/problem=284
# A 'steady square' is a number whose square ends in the same digits
# i.e. 76^2 = 5776 ends in '76', so 76 is a steady square
# Leading 0's aren't allowed
# Find the sum of the digits of all the n-digit steady squares in base 14
# for 1 ≤ n ≤ 10000 (decimal) and give your answer in base 14

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
    i=0
    while i < len(ans):
        if ans[i] >= base:
            if i<len(ans)-1:
                ans[i+1] += int(ans[i]/base)
                ans[i] = ans[i]%base
            else:
                ans.append(int(ans[i]/base))
                ans[i] = ans[i]%base
        i += 1
    while ans[-1] >= base:
        ans.append(int(ans[-1]/base))
        ans[-1] = ans[-1]%base
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
                    #if d == max_digits-1:
                    #    print(temp, total)
                    if n != 0:
                        total = plus(total,sum_of_digits(temp), base)
        if d % 100 == 0:
            print(d, total)
        ss = new_ss[::1]
    print(total)

def steady_squares_direct(max_digits=10000, base=14):
    ssd = []
    total = [1] #skip 1 because it leads immediately to an impossible inverse
    count = 0
    next_dig=[]
    squares = []
    for n in range(2,base): #setting up first digits is a little different
        temp = [n]
        squared = mult(temp,temp,base)
        if squared[:1] == temp:
            ssd.append(temp)
            total = plus(total,sum_of_digits(temp), base)
            #print(temp, total)
            if len(squared) > 1:
                next_dig.append(squared[1])
                squares.append(squared)
            else:
                next_dig.append(0)
    inv = {1:1, 3:5, 5:3, 9:11, 11:9, 13:13} #this is the only place base 14 is actually hardcoded in, but it could be generalized if there was a reason to
    a = [0]*len(ssd)
    for d in range(1,max_digits):
        if d%100==0:
            print(d)
        for i in range(len(ssd)):
            next_dig[i] = squares[i][d]
            a[i] = ((base-next_dig[i])*inv[(2*ssd[i][0]-1)%base])%base
            #next_dig[i] = mult(ssd[i],ssd[i])[d]#(((a[i]**2)%base)+int(2*a[i]*ssd[i][0]/base))%base
            sq = [0,0]*d + mult([a[i]],[a[i]],base)
            lin = [0]*d+mult(mult([a[i]],ssd[i],base),[2],base)
            squares[i] = plus(plus(sq, lin, base), squares[i], base)
            ssd[i]. append(a[i])
            #next_dig[i] = squares[i][d]
            #if i==0:
            #    print(next_dig[i])
            if d == max_digits-1:
                print(ssd[i])
    return(ssd)

#steady_squares(99)
print("next")
answer = steady_squares_direct(10000)
#n=[1]
#total = []
#for i in range(7**10):
#    if mult(n,n)[:len(n)] == n:
#        total = plus(total,sum_of_digits(n))
#        print(n, total)
#    n = plus(n,[1])
#    #print(n)
sums =[]
for a in answer:
    a.reverse()
    temp = list(filter(None, a))
    temp = [(i+1)*temp[i] for i in range(len(temp))]#these numbers aren't right, they need to change with the number of 0's so far
    sums.append([sum(temp)])
final = plus(plus(sums[0], sums[1],14),[1],14)
final.reverse()

printout = ''
d = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'a', 11:'b', 12:'c', 13:'d'}
for f in final:
    printout += d[f]
print(printout)
#print(final)
