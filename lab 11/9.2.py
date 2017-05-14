# Засько Б., КНИТ16-А

import string
import random

f2 = open('f2.txt', 'w')
for i in range(random.randint(5000, 10000)):
        f2.write(random.choice(string.digits))
f2.close()

f2 = open('f2.txt', 'r')
data = f2.read()
f2.close()

data2 = ''
for i in data:
    if i == '0':
        data2 += '1'
    elif i == '1':
        data2 += '0'
    else:
        data2 += i

g2 = open('g2.txt', 'w')
g2.write(data2)
g2.close()
