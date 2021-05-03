import csv

def num_value(word):
    return sum(list(map(lambda x: ord(x)-64, word)))
        

names = []
with open('p022_names.txt', 'r') as filehandle:
    namesreader = csv.reader(filehandle, delimiter=',', quotechar='"')
    names = [row for row in namesreader]
names = names[0]
names.sort()

scores = [(n+1)*num_value(names[n]) for n in range(len(names))]
print(sum(scores))


