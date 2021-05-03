with open("p079_keylog.txt") as f:
    content = [line.rstrip('\n') for line in f]

after = {}
#print(after)
for c in content:
    if int(c[0]) not in after.keys():
        after[int(c[0])] = []
    if int(c[1]) not in after.keys():
        after[int(c[1])] = []
    if int(c[2]) not in after.keys():
        after[int(c[2])] = []
    if int(c[1]) not in after[int(c[0])]:
        after[int(c[0])].append(int(c[1]))
    if int(c[2]) not in after[int(c[0])]:
        after[int(c[0])].append(int(c[2]))
    if int(c[2]) not in after[int(c[1])]:
        after[int(c[1])].append(int(c[2]))
k = list(after.keys())
k.sort(key=lambda x: len(after[x]), reverse=True)
print(k)
