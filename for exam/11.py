import random
import numpy as np

arr = np.zeros(10, dtype=int)
for i in range(len(arr)):
    arr[i] = random.randint(15, 30)
c = 0
for i in arr:
    if i > 21:
        c += 1
print("Days with a water temperature above 21:", c)
