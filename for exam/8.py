import numpy as np
import random

arr = np.zeros(15, dtype=int)
for i in range(len(arr)):
    arr[i] = random.randint(-15, 30)
print(arr)
m = max(arr)
for i in range(len(arr)):
    if arr[i] == m:
        break
print("Max element - A{}, value - {}".format(i, m))
