# Засько Б., КНИТ16-А
# Определитель квадратной матрицы (массива)

import numpy as np

a = np.arange(9).reshape((3, 3))
print("Квадратная матрица (массив) - ", a)
print("Определитель - ", np.linalg.det(a))


def determinant(m):
    size = len(m)
    if not m or not m[0]:
        return 1
    if size == 1:
        return m[0][0]
    if size == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]

    t = 0
    for i in range(size):
        arr = [[value for row, value in enumerate(line) if row != i] for line in m[1:]]
        t += (-1) ** i * m[0][i] * determinant(arr)

    return t
