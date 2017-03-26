# Засько Б., КНИТ16-А
# Бинарный поиск

from timeit import timeit
import numpy as np

x = int(input("Количество элементов массива: "))
a = np.arange(x)
s = int(input("Иcкомый элемент: "))
i = 0
j = len(a)-1
m = int(j/2)
while a[m] != s and i < j:
    if s > a[m]:
        i = m+1
    else:
        j = m-1
    m = int((i+j)/2)
if i > j:
    print("Элемент не найден")
else:
    print("Элемент найден в позиции", m+1)
