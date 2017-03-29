# Засько Б., КНИТ16-А
# Линейный поиск

from timeit import timeit

setup = '''
import numpy as np
x = int(input("Количество элементов массива: "))
s = int(input("Иcкомый элемент: "))
a = np.arange(x)
'''

stmt = '''
i = 0
N = len(a)
while i < N and a[i] != s:
    i += 1
if i == N:
    print("Элемент не найден")
else:
    print("Элемент найден в позиции", i+1)
'''
time = timeit(stmt, setup, number=1)
print("Время выполнения алгоритма: {:f} секунд".format(time))
