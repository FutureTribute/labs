import random
import numpy as np

arr = np.zeros(15, dtype=int)
for i in range(len(arr)):
    arr[i] = random.randint(-100, 100)
print(arr)
print(min(arr))
