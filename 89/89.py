with open("p089_roman.txt") as f:
    content = [line.rstrip('\n') for line in f]

value = {'I': 1, 'i':1, 'V':5, 'v':5, 'X':10, 'x':10, 'l':50, 'L':50, 'c':100, 'C':100, 'd':500, 'D':500, 'M':1000, 'm':1000}

def interpret(rn:str):
    total = 0
    while rn != '':
        current = rn[0]
        if len(rn) > 1 and value[rn[1]] > value[current]:
            total += value[rn[1]]-value[rn[0]]
            rn = rn[2:]
            #print(total)
        else:
            while rn != '' and rn[0] == current:
                total += value[current]
                #print(total)
                rn = rn[1:]
    return(total)

def encode(dn:int):
    rn = ''
    rn += 'M'*int(dn/1000)
    dn %= 1000
    c = int(dn/100)
    if c == 9:
        rn += 'CM'
    elif c >= 5:
        rn += 'L'
        rn += 'C'*(c-5)
    elif c == 4:
        rn += 'CL'
    else:
        rn += 'C'*c
    dn -= c*100
    x = int(dn/10)
    if x == 9:
        rn += 'XC'
    elif x >= 5:
        rn += 'D'
        rn += 'X'*(x-5)
    elif x == 4:
        rn += 'XD'
    else:
        rn += 'X'*x
    dn -= x*10
    if dn == 9:
        rn += 'IX'
    elif dn >= 5:
        rn += 'V'
        rn += 'I'*(dn-5)
    elif dn == 4:
        rn += 'IV'
    else:
        rn += 'I'*dn
    return(rn)
    
savings = 0
for c in content:
    #print(c)
    savings += len(c)-len(encode(interpret(c)))
    #print(savings)
print(savings)
