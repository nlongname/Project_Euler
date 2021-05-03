import decimal

values = {'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
blends = {0:'High Card', 1:'One Pair', 2:'Two Pairs', 3:'Three of a Kind', 4:'Straight', 5:'Flush', 6:'Full House', 7:'Four of a Kind', 8:'Straight Flush', 9:'Royal Flush'}

with open("p054_poker.txt") as f:
    content = [line.rstrip('\n') for line in f]

def card_value(n:str):
    if n in values.keys():
        return values[n]
    else:
        return int(n)

def hand_value(hand:list):
    flush = False
    straight = False
    numbers = []
    suits = []
    for card in hand:
        numbers.append(card[0])
        suits.append(card[1])
    suits = list(dict.fromkeys(suits))
    if len(suits) == 1:
        flush = True
    numbers = list(map(card_value, numbers))
    numbers.sort()
    if numbers[-1]-numbers[0] == len(numbers)-1 and len(list(dict.fromkeys(numbers))) == len(numbers):
        straight = True
    if straight and flush:
        if numbers[-1] == 14: #Ace
            return 9 #Royal Flush
        else:
            return 8 + decimal.Decimal(numbers[-1])/100
    elif straight:
        return 4 + decimal.Decimal(numbers[-1])/100
    elif flush:
        temp = 5
        for i in range(len(numbers)):
            temp += decimal.Decimal(numbers[0-i-1])/decimal.Decimal(10)**(2*(i+1))
        return temp
    counts = []
    for n in list(dict.fromkeys(numbers)):
        counts.append((n, numbers.count(n)))
    counts.sort(key = lambda x: x[1]) #sort by the counts of each 
    counts.reverse() #then reverse so you have the biggest count first
    if counts[0][1] == 4:
        temp = 7 #four of a kind
    elif counts[0][1] == 3:
        if counts[1][1] == 2:#Full House
            temp = 6
        if counts[1][1] != 2:
            temp = 3 #three of a kind
    elif counts[0][1] == 2:
        if counts[1][1] == 2:
            temp = 2 #two pair
        else:
            temp = 1 #one pair
    else:
        temp = 0
    for i in range(len(counts)): #adding the number of the cards as decimals for a tiebreaker
        temp += decimal.Decimal(counts[i][0])/decimal.Decimal(10)**(2*(i+1))
    return temp
        
one_count = 0
two_count = 0
for c in content:
    temp = c.split(' ')
    if hand_value(temp[:5]) > hand_value(temp[5:]):
        one_count += 1
    else:
        two_count += 1
print(one_count)
