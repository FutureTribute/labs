# import numpy as np
# import string

arr = [0] * 5
for i in range(len(arr)):
    # while True:
        arr[i] = input("Surname {}: ".format(i))
        # if set(arr[i]) in set(string.ascii_letters):
        #     break
        # else:
        #     print("Use only letters")
for i in arr:
    print(i)
