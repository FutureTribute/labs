import numpy as np
import random

arr = np.zeros(12, dtype=int)
for i in range(len(arr)):
    arr[i] = random.randint(-20, 10)
print(arr)
for i in range(len(arr)):
    if arr[i] < 0:
        arr[i] = 0
print(arr)
