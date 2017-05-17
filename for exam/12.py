import random
import numpy as np

arr = np.zeros(10, dtype=int)
for i in range(len(arr)):
    arr[i] = random.randint(-20, 10)
s = 0
for i in range(len(arr)):
    s += arr[i]
s /= len(arr)
c = 0
for i in arr:
    if i > s:
        c += 1
print("Days with a temperature above average temperature:", c)
