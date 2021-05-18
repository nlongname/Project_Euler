# https://projecteuler.net/problem=90
# Find all distinct pairs of dice with one-digit numbers on each face that
# can be used to show all positive square numbers below 100
# [1,2,3,4,5,6] is considered distinct from [1,2,3,4,5,9], but you can flip
# the 6 upside down to use it as a 9

import itertools
import functools

# there's only 10C6 = 210 dice, so there's no reason not to brute force
dice = [list(x) for x in itertools.combinations(range(10),6)]
for d in dice: #add in 6's or 9's when they can be flipped
    if 6 in d and 9 not in d:
        d += [9]
    if 9 in d and 6 not in d:
        d += [6]

squares = list(map(lambda x: x**2, range(1,10)))

def makes_squares(d:list):
    successes = []
    count = 0
    for i in range(len(d)):
        #limit j to prevent any repeated pairs, while 2 identical dice (i==j)
        for j in range(i,len(d)):
            #find every possible 2-digit number that can be made with these dice
            possible = [r[0]*10+r[1] for r in itertools.chain(itertools.product(d[i],d[j]), itertools.product(d[j],d[i]))]
            #check that our squares are in there
            in_there = [s in possible for s in squares]
            flag = functools.reduce(lambda x, y: x and y, in_there) #this seemed more readable than a double-negative lookup, but there might be a better way
            if flag:
                successes.append((i, j))
                count += 1
    return count

print(makes_squares(dice))
