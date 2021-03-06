# Засько Б., КНИТ16-А
# Найти сумму и произведение элементов квадратной матрицы; осуществить поиск элемента в квадратной матрице

import numpy as np


def sum_iter(a):
    """Итерационное нахождение суммы элементов квадратной матрицы
    
    :param a: исходная квадратная матрица
    :return: сумма элементов
    """
    s = 0
    for i in a:
        for j in i:
            s += j
    return s


def sum_rek(a):
    """Рекурсивное нахождение суммы элементов квадратной матрицы
    
    :param a: исходная квадратная матрица
    :return: сумма элементов
    """
    if type(a) != np.ndarray:
        return a
    elif len(a) == 0:
        return 0
    else:
        return sum_rek(a[0]) + sum_rek(a[1:])


def mul_iter(a):
    """Итерационное нахождение произведения элементов квадратной матрицы
    
    :param a: исходная квадратная матрица
    :return: произведение элементов
    """
    m = 1
    for i in a:
        for j in i:
            m *= j
    return m


def mul_rek(a):
    """Рекурсивное нахождение произведения элементов квадратной матрицы 
    
    :param a: исходная квадратная матрица
    :return: произведение элементов
    """
    if type(a) != np.ndarray:
        return a
    elif len(a) == 0:
        return 1
    else:
        return mul_rek(a[0]) * mul_rek(a[1:])


def sea_iter(a, x):
    """Итерационный поиск элемента по заданому значению в квадратной матрице
    
    :param a: исходная квадратная матрица
    :param x: искомый элемент
    :return: позиция элемента
    """
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i][j] == x:
                return i+1, j+1


def sea_rek(a, x, t, t2):
    """Рекурсивный поиск элемента по заданому значению в квадратной матрице
    
    :param a: исходная квадратная матрица
    :param x: искомый элемент
    :param t: позиция в строке
    :param t2: позиция в столбце
    :return: позиция элемента
    """
    def sea_rek2(a, x, t2):
        if a[0] == x:
            return t2 + 1
        else:
            t2 += 1
            return sea_rek2(a[1:], x, t2)

    if len(a) == 0:
        return None
    elif x in a[0]:
        y = sea_rek2(a[0], x, t2)
        return t+1, y
    else:
        t += 1
        return sea_rek(a[1:], x, t, t2)




while True:
    try:
        n = int(input("Размерность квадратной матрици: "))
        arr = np.zeros(n**2, dtype=int).reshape((n, n))
        for i in range(n):
            for j in range(n):
                while True:
                    try:
                        arr[i][j] = int(input("Элемент A{}{}: ".format(i+1, j+1)))
                        break
                    except ValueError:
                        print("Введены некоректные данные")
        print(arr)
        print("=======Сумма=======")
        print(sum_iter(arr))
        print(sum_rek(arr))
        print("=======Произведение=======")
        print(mul_iter(arr))
        print(mul_rek(arr))
        print("=======Поиск=======")
        el = int(input("Введите число для поиска: "))
        print(sea_iter(arr, el))
        p, p2 = 0, 0
        print(sea_rek(arr, el, p, p2))
        print("==============\n")
    except ValueError:
        print("Введены некоректные данные")
