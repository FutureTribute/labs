# Засько Б., КНИТ16-А
# Определитель квадратной матрицы (массива)

import numpy as np

a = np.arange(9).reshape((3, 3))
print("Квадратная матрица (массив) - ", a)
print("Определитель - ", np.linalg.det(a))
