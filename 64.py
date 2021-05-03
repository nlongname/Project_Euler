import math

def find_next(packet):
    (root, num, den) = packet
    new_den = (root-num**2)/den
    unit = int((math.sqrt(root)-num)/new_den)
    new_num = -num-unit*new_den
    return(unit, (root, int(new_num), int(new_den)))

def find_pattern_length(number):
    thread = []
    starting_point = int(math.sqrt(number))
    if starting_point**2 == number:
        return(0)
    r=number
    d=1
    n=-starting_point
    u, (r, n, d) = find_next((r,n,d))
    while (r, n, d) not in thread:
        thread.append((r, n, d))
        u, (r, n, d) = find_next((r,n,d)) #i don't think the unit matters
        #print(u) #besides this test
    return(len(thread))
        
        
def odd_periods(limit):
    count = 0
    for i in range(limit+1):
        if find_pattern_length(i) % 2 == 1:
            count += 1
    return(count)
print(odd_periods(10000))
