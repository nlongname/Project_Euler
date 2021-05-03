num = []
index = -1

with open('input.txt') as f:
    read_data = f.read()
while index != 0:
    num.append(int(read_data[:11])) #1 extra just to be safe, but carrying will almost certainly make it work regardless
    #print(num[-1])
    index = read_data.find('\n')+1
    read_data = read_data[read_data.find('\n')+1:]
print(str(sum(num))[:10])
print(str(sum(num)))
