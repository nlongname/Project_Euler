import math

def counting_rectangles(goal=2000000):
    #number of rectangles is the xth triangular number times the yth triangular number
    #because it's (x * x-1 * x-2 * ... * 1) * (y * y-1 * y-2 * ... * 1)
    #ways that you can arrange something that's 1, 2, 3, etc. ways across in x or y spaces
    #this can be calculated as x(x+1)/2 * y(y+1)/2 = goal
    #so x*y*(x+1)*(y+1) = 4*goal
    #upper limit: (xy)^2 ~= 4*goal (round up)
    #lower limit: [(x+1)(y+1)]^2 ~= 4*goal (round down)
    #solve each of these for y and we'll have a range for our given x
    distances={}
    min_distance = goal
    best_pair = (0, 0)
    for i in range(1,math.ceil(math.sqrt(math.ceil(math.sqrt(4*goal))))+1): #sounds insane, but we're trying to figure out what multiplies to the square root of 4*goal, and don't want to double-count, so we only go up (roughly) to the square root of /that/
        local_distance = goal
        best_j = 0
        for j in range(int(math.sqrt(4*goal)/(i+1)-1), math.ceil(math.sqrt(4*goal)/i)):
            temp = int(i*j*(i+1)*(j+1)/4)
            temp_distance = abs(temp-goal)
            if temp_distance < local_distance:
                local_distance = temp_distance
                best_j = j
                if local_distance == 0:
                    return(i*j)
        distances[(i, j)] = local_distance
        #print(i, j, local_distance)
        if local_distance < min_distance:
            min_distance = local_distance
            best_pair = (i, best_j)
            print(f"new best: {best_pair} is {min_distance} away")
    return(best_pair[0]*best_pair[1])
print(counting_rectangles())
