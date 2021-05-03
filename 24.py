def factorial(n): #didn't actually use this helper
    p = 1
    while n > 0:
        p *= n
        n -= 1
    return(p)

f = [1]
for i in range(1,10): #made a list of all the factorials I need here instead, f[n] == n!
    f.append(f[-1]*i)
limit = 1000000
current = 9 #current num of digits left to choose, we start with 9
answer = 0
left = list(range(10))
while len(left) > 0:
    d=0
    while f[current] < limit: #with n digits unchosen, there are n! combinations starting with each digit. subtract off however many you can
        limit -= f[current]
        d += 1
    answer = 10*answer + left.pop(d) #whatever d ends up at is the next digit of our answer, so put it into answer and move onto the next slot
    #print(answer)
    current -= 1 #we've decided one more digit, one fewer left to choose
print(answer)
