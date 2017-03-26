# Засько Б., КНИТ16-А
# Линейный поиск

from timeit import timeit
import numpy as np

x = int(input("Количество элементов массива: "))
a = np.arange(x)
s = int(input("Иcкомый элемент: "))
i = 0
N = len(a)
while i < N and a[i] != s:
    i += 1
if i == N:
    print("Элемент не найден")
else:
    print("Элемент найден в позиции", i)
