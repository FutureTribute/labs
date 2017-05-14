# Засько Б., КНИТ16-А

import random

a = []
for i in range(1, 1001):
    a.append(i)
for i in range(-1000, 0):
    a.append(i)
random.shuffle(a)
f = open('f.txt', 'w')
for i in a:
    f.write(str(i) + ' ')
f.close()

f = open('f.txt', 'r')
data = f.read()
f.close()

data = data[0:-1]
data = data.split(' ')
for i in range(len(data)):
    data[i] = int(data[i])
data.sort()
for i in range(len(data)):
    if data[i] > 0:
        break
data2 = data[:i]
data = data[i:]
data_end = []
for i in range((len(data) + len(data2))//4):
    for j in range(2):
        data_end.append(str(min(data)) + ' ')
        data.remove(min(data))
    for j in range(2):
        data_end.append(str(min(data2)) + ' ')
        data2.remove(min(data2))

g = open('g.txt', 'w')
for i in data_end:
    g.write(i)
g.close()
