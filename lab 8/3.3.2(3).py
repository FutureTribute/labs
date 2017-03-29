# Засько Б., КНИТ16-А
# Алгоритм Вагнера-Фишера

from timeit import timeit
import numpy as np

S = input("Введите строку: ")
subS = input("Введите вторую строку: ")

m = len(S)
n = len(subS)
d = np.zeros((m, n))
for i in range(m):
    d[i, 0] = i
for j in range(n):
    d[0, j] = j
for j in range(1, n):
    for i in range(1, m):
        if S[i] == subS[j]:
            d[i, j] = d[i - 1, j - 1]
        else:
            d[i, j] = min(d[i - 1, j] + 1, d[i, j - 1] + 1, d[i - 1, j - 1] + 1)
print("Расстояние между строками: ", int(d[m - 1, n - 1]))
