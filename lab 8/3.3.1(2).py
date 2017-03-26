# Засько Б., КНИТ16-А
# Бинарный поиск

from timeit import timeit
import numpy as np

x = int(input("Количество элементов массива: "))
a = np.arange(x)
s = int(input("Иcкомый элемент: "))
i = 0
j = len(a) - 1
while i <= j:
    m = int((i + j) / 2)
    if s > a[m]:
        i = m+1
    elif s < a[m]:
        j = m-1
    else:
        break
if i > j:
    print("Элемент не найден")
else:
    print("Элемент найден в позиции", m)
