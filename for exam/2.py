import numpy as np

arr = np.zeros(5, dtype=int)
for i in range(len(arr)):
    while True:
        try:
            arr[i] = int(input("Value for A{}: ".format(i)))
            break
        except ValueError:
            print("Only int numbers")
for i in arr:
    print("For {}: Square: {}, Square root: {:f}".format(i, i**2, i**(1/2)))
