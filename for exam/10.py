import random
import numpy as np

arr = np.zeros(10, dtype=int)
for i in range(len(arr)):
    arr[i] = random.randint(-20, 8)
c = 0
for i in arr:
    if i < -10:
        c += 1
print("Days with temperatures below -10:", c)
