def dice_sums(sides, dice):
    if dice == 0: return [0]
    totals = [0]*(sides*dice+1)
    d=1
    for i in range(1,sides+1):
        totals[i] += 1
    while d < dice:
        old_totals = totals
        totals = [0]*len(totals)
        for i in range(len(totals)):
            if old_totals[i] > 0:
                #totals[i] += old_totals[i]-1
                for j in range(1,sides+1):
                    totals[i+j] += old_totals[i]
        d += 1
    return totals

def chance_first_wins(first=(4,9),second=(6,6)):
    first_dist = dice_sums(first[0],first[1])
    second_dist = dice_sums(second[0],second[1])
    second_sum = 0
    cases = 0
    for i in range(len(first_dist)):
        if i > 0 and i-1 < len(second_dist):
            second_sum += second_dist[i-1]
        cases += first_dist[i]*second_sum
    return cases/sum(first_dist)/sum(second_dist)
        
print(chance_first_wins())
