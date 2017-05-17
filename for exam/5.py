import numpy as np
import random

arr = np.zeros(7, dtype=int)
for i in range(len(arr)):
    arr[i] = random.randint(1, 10)
print(arr)
print("*2:")
print(arr * 2)
