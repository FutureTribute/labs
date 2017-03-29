# Засько Б., КНИТ16-А
# Алгоритм Бойера-Мура-Хорспула

from timeit import timeit
import numpy as np

S = input("Введите строку: ")
subS = input("Введите подстроку: ")

n = len(S)
m = len(subS)
d = [m] * (ord(max(max(S), max(subS))) + 1)
for i in range(m - 1):
    d[ord(subS[i])] = m - i - 1
pos = -1
i = 0
while n - i >= m and pos == -1:
    j = m - 1
    while S[i + j] == subS[j]:
        if j == 0:
            pos = i
            break
        j -= 1
    i += d[ord(S[i + m - 1])]
if pos != -1:
    print("Элемент найден в позиции", pos)
else:
    print("Элемент не найден")
