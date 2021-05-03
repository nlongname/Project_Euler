found = [1,40755]#,1533776805,57722156241751, 2172315626468283465]

def find_triple(triangle=[1], pentagon=[1], hexagon=[1]):
    t = t_count = 1
    p = p_count = 1
    h = h_count = 1
    while t in found or (not t==p==h): #goes until it finds one new set
        #if t==p==h:
        #    print(t,t_count, p_count, h_count)
        if t <= p and t <= h: #if it's not, increase the smallest one and check again
            t = t + t_count + 1
            t_count += 1
        elif p <= t and p <= h:
            p = p + 3*p_count+1
            p_count += 1
        else:
            h = h + 4*h_count + 1
            h_count += 1
    print(t)
    found.append(t)
    return(t, t_count, p_count, h_count)

ans, tri, penta, hexa = find_triple()
