coins = [200, 100, 50, 20, 10, 5, 2, 1]
record = {}
def coin_sums(amt=200, coins = [200, 100, 50, 20, 10, 5, 2, 1]): #coins are assumed to include pennies
    #print(amt)
    if amt in record.keys():
        return(record[(amt, coins[0])])
    options = list(filter(lambda x: x<=amt, coins))
    ways = 0
    #print(options[:-1])
    for c in options[:-1]: #ignoring pennies for now
        for i in range(1,int(amt/c)+1):
            ways += coin_sums(amt - (i*c), options[options.index(c)+1:])
    ways += 1 #the last way is always finishing up with all pennies
    record[(amt, coins[0])] = ways
    return(ways)
print(coin_sums(200))

