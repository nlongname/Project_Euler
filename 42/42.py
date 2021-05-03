import csv, math

def num_value(word):
    return sum(list(map(lambda x: ord(x)-64, word)))
        

with open('p042_words.txt', 'r') as filehandle:
    wordsreader = csv.reader(filehandle, delimiter=',', quotechar='"')
    words = [row for row in wordsreader]
words = words[0]
words = list(map(num_value, words))

maximum = max(words)
max_triangle_n = int(math.sqrt(2*maximum))#figuring out how many triangular numbers I need to check
triangles = [1]
n=1
t=1
while n < max_triangle_n:
    n += 1
    t += n
    triangles.append(t)
print(len(list(filter(lambda x: x in triangles, words))))
