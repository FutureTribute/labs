# Засько Б., КНИТ16-А
# Алгоритм Вагнера-Фишера

from timeit import timeit

setup = '''
import numpy as np
S = input("Введите список: ")
S = S.split(",")
subS = input("Введите искомую строку: ")
R = int(input("Значение разницы: "))
n = len(subS)
li = []
'''

stmt = '''
for el in S:
    m = len(el)
    d = np.ones((m + 1, n + 1))
    for i in range(1, m + 1):
        d[i, 0] = i
    for j in range(1, n + 1):
        d[0, j] = j
    for j in range(1, n):
        for i in range(1, m):
            if el[i] == subS[j]:
                d[i, j] = d[i - 1, j - 1]
            else:
                d[i, j] = min(d[i - 1, j] + 1, d[i, j - 1] + 1, d[i - 1, j - 1] + 1)
    if d[m - 1, n -1] - 1 <= R:
        li.append(el)
print("Подходящие варианты: ", li)
'''
time = timeit(stmt, setup, number=1)
print("Время выполнения алгоритма: {:f} секунд".format(time))
