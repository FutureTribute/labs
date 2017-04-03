# Засько Б., КНИТ16-А
# Произведение двух квадратных матриц (массивов), учитывая размерность

import numpy as np

s1 = int(input("Количество строк первой матрицы: "))
s2 = int(input("Количество столбцов первой матрицы: "))
c1 = int(input("Количество строк второй матрицы: "))
c2 = int(input("Количество столбцов второй матрицы: "))
if s2 == c1:
    a = np.arange(s1*s2).reshape((s1, s2))
    b = np.arange(c1*c2).reshape((c1, c2))
    print("Первая матрица - \n", a)
    print("Вторая матрица - \n", b)
    C = np.zeros((s1, c2), dtype=int)
    zx = list(zip(*b))
    for i in range(s1):
        for j in range(c2):
            z1 = list(a[i])
            z2 = zx[j]
            k = 0
            while k < s2 or k < c1:
                C[i][j] += z1[k] * z2[k]
                k += 1
    print("Результат произведения матриц - \n", C)
else:
    print("Умножение матриц при заданых условиях невозможно")
