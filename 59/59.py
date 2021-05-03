import csv, math

with open("p059_cipher.txt", newline='') as f:
    content = list(csv.reader(f, delimiter=','))
content = content[0]
content = list(map(int, content))
word_list = ['the', 'be', 'to', 'of', 'and', 'in', 'that', 'have', 'it', 'for']

def to_bin(n:int):
    result=[0]*8
    while n > 0:
        d = int(math.log(n,2))
        result[d] = 1 #note: the binary numbers will appear "backwards", but be easier to work with
        n -= 2**d
    return result

def xor(a:int, b:int):
    a = to_bin(a)
    b = to_bin(b)
    for i in range(8):
        a[i] += b[i]
        a[i] %= 2
    return(to_dec(a))

def to_dec(l:list):
    n = 0
    for i in range(8):
        n += l[i]*2**i
    return(n)

def find_key(stuff:list):
    offset = len(stuff) % 3
    stuff += offset*[0]
    max_count = 1
    for i in range(97,123):
        print(i)
        for j in range(97,123):
            for k in range(97,123):
                temp = []
                for l in range(0,len(stuff),3):
                    temp.append(xor(stuff[l],i))
                    temp.append(xor(stuff[l+1],j))
                    temp.append(xor(stuff[l+2],k))
                string = ''
                for t in temp:
                    string += chr(t)
                count = 0
                for w in word_list:
                    if w in string:
                        count += 1
                if count == len(word_list):
                    print(f"count is {count} out of {len(word_list)} and beginning is \'{string[:10]}\'")
                    print(sum(temp))

find_key(content)
