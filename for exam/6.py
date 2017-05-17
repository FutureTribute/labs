import numpy as np
import random

arr = np.zeros(8, dtype=int)
for i in range(len(arr)):
    arr[i] = random.randint(-10, 10)
print(arr)
c = 0
for i in arr:
    if i < 0:
        c += 1
print("Negative elements", c)
