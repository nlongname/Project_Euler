import math

with open("p099_base_exp.txt") as f:
    content = [line.rstrip('\n') for line in f]
#content = [x.strip() for x in content]
content = [(int(x[:x.index(',')]), int(x[x.index(',')+1:])) for x in content]
print(content.index(max(content,key=lambda x: x[1]*math.log(x[0])))+1)
